from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "staff_members" (
    "id" UUID NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "role" VARCHAR(8) NOT NULL DEFAULT 'employee',
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
COMMENT ON COLUMN "staff_members"."role" IS 'EMPLOYEE: employee\nADMIN: admin';
        ALTER TABLE "users" DROP COLUMN "role";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" ADD "role" VARCHAR(5) NOT NULL DEFAULT 'user';
        COMMENT ON COLUMN "users"."role" IS 'USER: user\nADMIN: admin';
        DROP TABLE IF EXISTS "staff_members";"""


MODELS_STATE = (
    "eJztmOtv2kgQwP8Vy59yUi5KKNAoOp1kEkflGqBK4B7tVdbiHWCV9a5rr5uiiP/9dhe/Hw"
    "jS5EoqviCYB975jccz40fT4xhoeHIn0Gw2AG8KgXlhPJoMeSC/1KmPDRP5fqZUAoGmVNuH"
    "ytDxtKXWoGkoAuQKqZwhGoIUYQjdgPiCcCalLKJUCbkrDQmbZ6KIkS8ROILPQSz0uT59lm"
    "LCMHyDMPnp3zszAhQXjk2wuraWO2Lpa9lk0r+61pbqclPH5TTyWGbtL8WCs9Q8igg+UT5K"
    "NwcGARKAc2GoU8ZhJ6L1iaVABBGkR8WZAMMMRVTBMH+bRcxVDAx9JfXR/t3cAY/LmUJLmF"
    "AsHlfrqLKYtdRUl7p8Z90even+oqPkoZgHWqmJmCvtiARau2quGUg3ABW2g0QV6JXUCOJB"
    "PdSiZwkujl1Pki9PgZwIMsrZHZZgTvA9jakpY8AjRpdxBjcwHvcH9t3YGnxQkXhh+IVqRN"
    "bYVpqWli5L0qN1Srisj3X1pH9i/NUfvzPUT+PjaGiXE5fajT+a6kwoEtxh/MFBOHezJdIE"
    "jLTMEhv5+ImJLXoeEvtDExsfPstrwClUM3q5QIHNIk9ntC9RIOZCJbOJbymnEtxLZdEEz6"
    "d8CVB98Jn24MPN6B/bvjASo3+ZdTXoDy8MhD3CzO0y7aFvDgU2Fwv583xDov+0bvWD8ryU"
    "u2GsaCnNqlhEIQROXa/pM9FQPJlHibI88J7Wylxd59fWWftt+/xNt30uTfRZUsnbDVT7w7"
    "GEphr17L62wygiVYDXPAAyZ+9hWbllS9ziCWUS/83+8Vsl90AizQo5QA/p8JK/NWR4MigQ"
    "69q17i6tK9vUEKfIvX9AAXYKNJWGt3hJktpWVV7LK0sQQ3Mdv4pCnTkPtmYkTIA3z4IqoD"
    "2bARvrctuSjBP3fbPfj6/Hw8j3008Gh5HvJ01sZeQLo0B/rZ366hOac/n/hr3vzF9hkOu2"
    "t5jkuu3GUU6pirOcRzCm4OxKsuR2oLmmCR4idBeOqcPrJNjqdLdAKK0aGWpdEaKPwvCBBz"
    "VzTDPHvM/rRHnW2mZLk1aNKLWuiJKEjhxAydea2u5xufYi1jAX5v1KPKfS8aWApjPjc78L"
    "7I1GN4W21uuPSxwng54tAWu80ois15CGRa55Kck1qNxL4Rr+sff1+1ugSIdaZV3/Hnr/bu"
    "WmZW/1kiuaBQFxF2bNkhZrjjetaSizOexpz/lUe+E97avcruNi2bY55FxeZ29odTpbtdnO"
    "hjbbKfcGVRo7QIzNXyfAs9PTbZrr6Wlzc1W6IkB5RQGsZqv84240bHhVkLmUQE6YDPATJq"
    "44NigJxef9xLqBooq60GITeEcD6+8y18ubUa+8Eqo/6O3WbJ+/vaz+A9leqBE="
)
