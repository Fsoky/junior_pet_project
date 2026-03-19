# Junior backend pet-project

**Стек**

- Python 3.10
- FastAPI
- Tortoise ORM
  - PostgreSQL (asyncpg)
  - aerich (migrations)
- Pydantic
- Redis
- PyJWT

**Структура проекта**

```
├── certs
├── src
│   ├── api
│   │   ├── core
│   │   │   ├── utils
│   │   ├── routers
│   │   │   ├── v1
│   │   │   │   ├── routers
│   │   │   │   ├── schemas
│   │   │   │   ├── services
│   ├── core
│   ├── db
│   │   ├── migrations
│   │   │   ├── models
│   │   ├── models
│   │   ├── schemas
│   │   ├── utils
├──.env
├──.gitignore
├──.python-version
├──pyproject.toml
├──README.md
├──uv.lock
```

**Описание проекта**

Реализация бекенд логики с использованием FastAPI.
Регистрация, аутентификация и авторизация пользователя с использованием JWT.

**Система прав доступа, роли**

В проекте имеется база данных с таблицами User и StaffMember.

- User - обычный пользователь приложения, который может зарегестрироваться в системе, произвести вход и выход из системы. После аутентификации, авторизированный пользователь может изменять свои данные в системе или удалить свой аккаунт (мягкое удаление).
- StaffMember - Аутентифицированный пользователь, который был назначен администратором (admin/superadmin) в качестве сотрудника (employee).
  Сотрудник имеет доступ к просмотру своих данных, в то время, как администраторы или супер-администраторы могут манипулировать данными сотрудников

Система ролей проекта устроена иерархически: пользователь с ролью X может выполнять действия над пользователями с ролями, расположенными ниже по иерархии, но не над ролями, находящимися выше.

```
⭐ superadmin
    ⨽ admin
      ⨽ employee
```

- Супер-админ (superadmin) - может добавлять/удалять админов и сотрудников
- Админ (admin) - может добавлять/удалять сотрудников
- Сотрудник (employee) - просмотр своих данных

> [!TIP]
> Супер-админ назначается в ручную, в базе данных.

## Подготовка проекта к запуску

**.env**

```bash
DB_URL=asyncpg://postgres:toor@localhost:5432/juniordb
```

**Виртуальное окружение**

```bash
uv sync # pip install uv
```

**Миграции**

> [!TIP]
> Т.к. миграции уже имеются, нам остается только сделать обновление БД (после ее создания) \
> _Если нужно создать новые: `uv run -m aerich migrate`_

```bash
uv run -m aerich upgrade
```

**Запуск проекта**

> [!WARNING]
> Перед запуском нужно иметь запущеннный redis-server, а также иметь созданные ключи для JWT (private, public)

```bash
uv run -m src.__main__
```

**Swagger**

```bash
https://localhost:8000/docs
```

## Акцент на моментах

- Pydantic схема. Зачем там метод as_form?

Мне приходилось работать с фронтендом и я знаю, что на фронт части чаще всего используют форму (form), но почему нельзя было сразу подставить `Form(...)` к атрибуту в схеме? (потому что возможно так нельзя сделать, точно не помню) - В моем понимании, так будет удобнее использовать зависимость, а также на вход принимать параметры, которые не соответствуют нашей форме, пример ниже.

```python
class UserReigstrationSchema(BaseUserSchema):
    surname: Annotated[str, MinLen(1), MaxLen(64)]
    middle_name: Annotated[str, MinLen(2), MaxLen(64)]
    email: EmailStr
    password: Annotated[str, MinLen(6), MaxLen(128)]
    password_repeat: Annotated[str, MinLen(6), MaxLen(128)]

    @classmethod
    def as_form(
        cls,
        surname: str = Form(...),
        middleName: str = Form(...), # тут
        email: str = Form(...),
        password: str = Form(...),
        passwordRepeat: str = Form(...) # тут
    ) -> UserReigstrationSchema:
        return cls(
            surname=surname,
            middle_name=middleName,
            email=email,
            password=password,
            password_repeat=passwordRepeat
        )
```

Фронтендеры любят camelCase, а мы python_бекендеры любим sneak_case. Мы принимаем форму от фронта с его camelCase и возвращая (return cls), получаем наш любимый и верный sneak_case, а дальше можем его спокойно валидировать, проверять и т.п. А также при таком решении удобно принимать UploadFile.

- Хеширование пароля при регистрации

```python
hashed_password = bcrypt.hashpw(schema.password.encode(), bcrypt.gensalt())
updated_schema = schema.model_copy(update={"password": hashed_password.decode()})
```

- Mypy ругается

Единственное на что ругается mypy, так это на enum `Role`. Внутри прописана логика для magic методов lt gt, которые принимают Role.

```
This violates the Liskov substitution principle
```

```python
def __lt__(self, other: Role) -> bool:
    if not isinstance(other, Role):
        return NotImplemented
    return _order[self.value] < _order[other.value]
```

Почему так? - Этот enum создан для `CharEnumField` tortoise-orm, а черепаха принимает насколько мне известно только StrEnum
Решений у этой проблемы несколько:

1. Вместо Role указать str и ругаться не будет. Но это такой себе вариант, будто логически не соответствует.
2. Написать метод `has_permission(role: Role)` и делать проверку там.

```python
_order = {...}

class Role:
  ...

  def has_permission(self, other: Role) -> bool:
    return self._order[self.value] >= self._order[other.value]

# Usage
admin.role.has_permission(employee.role)
```

Но я пока что оставил как есть, возможно перепишу.

## Мысли в слух

Привет, меня зовут Даниил. Мысли в слух - это пару слов об этом проекте. \
Хоть я уже и год стараюсь практиковать FastAPI, этот проект был интересен своим ТЗ, прочитав его, я уже начал понимать как я буду его делать, единственный вопрос это: как нормально реализовать аутентификацию и авторизацию пользователя, никогда нигде мне такого не приходилось делать, ибо уклон был на Telegram mini-apps, где JWT по своей сути и не нужен был. Я начал изучать эту тему на канале Сурена, спасибо ему за гайды (https://www.youtube.com/@SurenKhorenyan). С помощью его ролика я смог реализовать эту систему в этом проекте.

Какие мысли у меня возникали в ходе разработки? Стандартные вопросы по структуре проекта, где должен быть этот файл, а где этот, а правильно ли я делаю и т.п.. Но, если вы возможно читаете это, значит проект был завершен.
Также я думал на счет refresh_token, но так и не понял зачем он здесь нужен,
возможно как нибудь я реализую и его.

Самое инетерсное, то что в начале я не думал как я буду делать logout, но потом с этим возникли проблемы из-за недостатка опыта. Погуглив, я пришел к мнению использовать redis для хранения jti с одним из статусов: alive и dead.
Пользователь входит в систему, статус alive, выходит - dead. Конечно через какое-то время эта запись удаляется из redis (по окончанию жизнидеятельности токена). Но возможно есть и другой способ это реализовать.

Было инетерсно реализовывыть pydantic схемы, недавно заметил, что атрибуты теперь можно делать с `Annotated[..., ...]` вместо `Field(...)`

Ну вроде больше нечего сказать, было классно. upd: А также познакомился с bcrypt.

Спасибо, \
с уважением Даниил

**Связь:**

Почта: cyberuest0x12@gmail.com \
Telegram: @fsoky (https://t.me/fsoky) \
YouTube: https://youtube.com/@fsoky
