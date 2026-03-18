from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "staff_members" ALTER COLUMN "role" TYPE VARCHAR(10) USING "role"::VARCHAR(10);
        COMMENT ON COLUMN "staff_members"."role" IS 'EMPLOYEE: employee
ADMIN: admin
SUPERADMIN: superadmin';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        COMMENT ON COLUMN "staff_members"."role" IS 'EMPLOYEE: employee
ADMIN: admin';
        ALTER TABLE "staff_members" ALTER COLUMN "role" TYPE VARCHAR(8) USING "role"::VARCHAR(8);"""


MODELS_STATE = (
    "eJztmFtv2jAUgP9KlKdO6qqSAauqaVJoM42pQFVg9ykysQGrjp0lzjpU8d9nm4TcWejKVi"
    "ZeUDiX2P6OnXOO73WXQUSCkyEH02kPuRPk6+favU6Bi8RDmfpY04HnJUop4GBClH0gDW1X"
    "WSoNmATcBw4XyikgARIiiALHxx7HjAopDQmRQuYIQ0xniSik+HuIbM5miM/VvL58E2JMIf"
    "qJgvivd2tPMSIwM20M5dhKbvOFp2TjcffyjbKUw01sh5HQpYm1t+BzRtfmYYjhifSRuhmi"
    "yAccwdQy5CyjZcei1YyFgPshWk8VJgKIpiAkEob+ahpSRzLQ1Ejyp/la3wKPw6hEiymXLO"
    "6Xq1Ula1ZSXQ518da8OXrRfqZWyQI+85VSEdGXyhFwsHJVXBOQjo/ksm3Ai0AvhYZjF5VD"
    "zXrm4MLI9SR+eAjkWJBQTnZYjDnG9zCmulgDHFCyiCK4gfGo27OGI7N3LVfiBsF3ohCZI0"
    "tqDCVd5KRHq5AwcT5Wp2f9Eu1Dd/RWk3+1z4O+lQ/c2m70WZdzAiFnNmV3NoCpzRZLYzDC"
    "Mgls6MEHBjbreQjsPw1sNPkkrj4jqBjRiznwLRq6KqJdgQJQBxUiG/vmYirA7SqKOnI9wh"
    "YIFT98utW7vhp8sqxzLTb6Ss3LXrd/rgHoYvqVDsfX1k0kCkJPzE7K9Xo7wAU/bYLojM/F"
    "38bphh3w3rxRX9DGaS6q/UhjKNUye74C5NtlaahLecW5SjxyARBz3k0S+sNDNJOjPDcazZ"
    "fNsxft5pkwUTNZS15uoNrtjwQymcGnt6nUIwUT4NzeAR/aBQ0zWGmakuyKqAcUjZj4Kez6"
    "HN+oyBlHL3lqnJfxTomlyRA+uFtXP+kNJBYnloT46vCbwwvz0tKXGbZZlFLlGm5eAiiYqS"
    "XJmcl5pFGV1IkxwuoCUU7yiRWGlSey7mGMgrHvZ/FQB/735cKhDvxPA1uoA4PQV4+lpWB5"
    "QFMuf68C/MP4Zaq4drNGFdduVlZxUpWt4lwMIUH2tiRzbgeaK5rIBZhsw3HtsJ8EjVa7Bk"
    "JhVclQ6bIQPRAEd8wvqWOqOaZ99hNlwzir06EZZ9UtmtRlUeLAFgUo/lFytjtM9MKAVtSF"
    "ab8cz4lw3BXQdc342BeEncHgKpPWOt1RjuO417EEYIVXGOFVa/EITdyGpiSVzVLXyiXBit"
    "zjfu8GEaDoFMNTfp/9m2BF3P/i5q9q+ZZb9mkm8rEz10s6tUhzvKlXA4nNoVl7zE/bjpu1"
    "H6LFjrZ/3QyRctnPBGG0WrVybWtDrm3lE4Q8GltAjMz3E2DjtN4d6KZL0MItqBiRI1rSWr"
    "4bDvoV9wWJSw7kmIoFfoHY4ccawQH/9jSxbqAoV53JszG8o575Mc/14mrQyfeF8gWdHWbc"
    "Wull+QsIZLDz"
)
