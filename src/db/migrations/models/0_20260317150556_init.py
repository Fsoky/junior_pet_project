from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "surname" VARCHAR(64) NOT NULL,
    "middle_name" VARCHAR(64) NOT NULL,
    "email" VARCHAR(256) NOT NULL,
    "password" VARCHAR(128) NOT NULL,
    "is_active" BOOL NOT NULL DEFAULT True
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztl1FP2zAQx79KlScmMVSytqC9tawTnWg7QdgmEIrc2E0tHDvEDqVC/e6znaRO0iZqEQ"
    "gq8Zb87y6++10S+56tgEFE+NE1R5H1vfFsURAgeVHQDxsWCEOjKkGACdGOsfTQCphwEQFP"
    "SHEKCEdSgoh7EQ4FZlSqNCZEicyTjpj6RoopfoiRK5iPxEwncnsnZUwhekI8uw3v3SlGBB"
    "byxFCtrXVXLEKtDaj4qR3VahPXYyQOqHEOF2LG6MobU6FUH1EUAYHU40UUq/RVdmmZWUVJ"
    "psYlSTEXA9EUxETkyt2Sgceo4iez4bpAX63y1T5unbROv3Vap9JFZ7JSTpZJeab2JFATGD"
    "nWUtuBAImHxmi4eRFSxbpArPP7IS0CB2gzxGJkCSZMQ4+yizLaDGQd20wwcM0L9Up0ZQ1w"
    "TMkibVwNSmcw7F853eFvVUnA+QPRiLpOX1lsrS5K6kHni9KZ/BySj2T1kMbfgXPeULeNm/"
    "GorwkyLvxIr2j8nBtL5QRiwVzK5i6AuXcsUzMw0tM0Ng7hCxtbjPxs7Ls2Nk3e9JXHkb5c"
    "a+rZDESbG5oLKXVTIvug/QvAk0sQ9cVM3nZaNf370708O+9eHnRapZ6MUoutTcsCxQBDSJ"
    "C7K8lS2CfNhCYKACa7cFwF7CdBu93ZAqH0qmSobUWIIeB8zqIN55hqjvmY/UR5bJ9ugVJ6"
    "VaLUtiJKzF15AMWPG77tHmMEAVpxLszHlXhOZOBbAV2dGV8EtIZfbzy+KGxrvYFT4ng97P"
    "UlYI1XOmGBzMFRnban97lzoxImwLufgwi6axZmsyrfdVNgB2UFUOBrQqpOVVU6fHRRhL2Z"
    "tWEsSS2HdYMJMD6fk8lrfsdvPJk8ynlSpbTD7zAXsp9/Q7vd3mpjaddsLO3y31B9GjtATN"
    "33E+Bxs7nNdtJsVm8nylYEKFcUiG6Yo35djUcVw7EJKYG8prLAW4g9cdggmIu7j4m1hqKq"
    "urCpZPAOht1/Za5nF+NeeQhSD+i99/ay/A8Ftwsv"
)
