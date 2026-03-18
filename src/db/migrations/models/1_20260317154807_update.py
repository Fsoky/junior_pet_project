from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" ADD "role" VARCHAR(5) NOT NULL DEFAULT 'user';
        COMMENT ON COLUMN "users"."role" IS 'USER: user\nADMIN: admin';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" DROP COLUMN "role";"""


MODELS_STATE = (
    "eJztmPFP4jAUx/+VZT95iWdwB2j8DZSLXAQuCncXPbOUtUBj1861U4nhf7+22+g2NgJGT0"
    "n8bfu+99b3Pq+lLc+2zyAi/GDEUWifWM82BT6SDzl937JBEBhVCQKMiXaMpIdWwJiLEHhC"
    "ihNAOJISRNwLcSAwo1KlESFKZJ50xHRqpIji+wi5gk2RmOlEbm6ljClET4inr8GdO8GIwF"
    "yeGKqxte6KeaC1LhXftaMabex6jEQ+Nc7BXMwYXXpjKpQ6RRSFQCD1eRFGKn2VXVJmWlGc"
    "qXGJU8zEQDQBERGZcjdk4DGq+MlsuC5wqkb56hzWj+rH35r1Y+miM1kqR4u4PFN7HKgJ9I"
    "f2QtuBALGHxmi4eSFSxbpArPI7kxaBfVQOMR9ZgAmT0IP0oYg2BbmObSoYuGZCvRJdWQMc"
    "UDJPGrcG5bDb61wNW72fqhKf83uiEbWGHWVxtDovqHvNL0pncjnEi2T5Eet3d3huqVfret"
    "DvaIKMi2moRzR+w2tb5QQiwVzKHl0AM3MsVVMw0tM0NgrgCxubj/xs7Ls2Nkne9JVHoX5c"
    "aerpDITlDc2EFLopkX3Q/vngySWITsVMvjbra/r3q3V5et663GvWCz3pJxZHmxY5ij6GkC"
    "B3W5KFsE+aMU3kA0y24bgM2E2CTqO5AULpVclQ2/IQA8D5IwtLzjHVHLMxu4ny0DneAKX0"
    "qkSpbXmUmLvyAIofStZ2mzGCAK04F2bjCjzHMvCtgC7PjC8CuoZfezC4yG1r7e6wwHHUa3"
    "ckYI1XOmGBsgdHwzSU3MqnZodGvubZlWkB6qEVrmns/5ui+jpirzC1R1edyxNLGf/S1lmv"
    "2z+xAPQxtV8wdRsbTNxG5bRtqEmrrjOTu8zBXAlj4N09ghC6KxbmsCrfVZPv+EUFUDDVwF"
    "R5KvvkdtdCIfZmdsm9L7Hsr7v5AePzefV7zR/KN776PcgLu0ppi/0mE7Kb243T2GTVSq81"
    "O3ejuN2opbEFxMR9NwEe1mqb7Ne1WvV+rWx5gHJEgWjJRfXH1aBf8e+DCSmAHFFZ4A3Ent"
    "i3CObi9mNiXUNRVZ3btVN4e73WnyLX04tBu3jLVB9ov/f2svgHAbZ7pQ=="
)
