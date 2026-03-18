from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "staff_members" DROP CONSTRAINT IF EXISTS "fk_staff_me_users_93a8750c";
        ALTER TABLE "staff_members" ADD CONSTRAINT "fk_staff_me_users_93a8750c" FOREIGN KEY ("user_id") REFERENCES "users" ("id") ON DELETE CASCADE;
        CREATE UNIQUE INDEX IF NOT EXISTS "uid_staff_membe_user_id_52b962" ON "staff_members" ("user_id");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "staff_members" DROP CONSTRAINT IF EXISTS "staff_members_user_id_key";
        DROP INDEX IF EXISTS "uid_staff_membe_user_id_52b962";
        ALTER TABLE "staff_members" DROP CONSTRAINT IF EXISTS "fk_staff_me_users_93a8750c";
        ALTER TABLE "staff_members" ADD CONSTRAINT "fk_staff_me_users_93a8750c" FOREIGN KEY ("user_id") REFERENCES "users" ("id") ON DELETE CASCADE;"""


MODELS_STATE = (
    "eJztmG1v4jgQgP9KlE89qVe1LLBVdToptDktpwKrFu5l91aRiQ1Ydexs4mwXVfz385iEvH"
    "OhW/bKii8I5gV7nrEzM3kyPYEJC8/uJZrNBsSbksC8Mp5MjjyivlSpTw0T+X6qBIFEU6bt"
    "QzB0PG2pNWgaygC5UilniIVEiTAJ3YD6kgqupDxiDITCVYaUz1NRxOnniDhSzIlc6H19/K"
    "TElGPylYTJT//BmVHCcG7bFMPaWu7Ipa9lk0n/5jdtCctNHVewyOOptb+UC8E35lFE8Rn4"
    "gG5OOAmQJDgTBuwyDjsRrXesBDKIyGarOBVgMkMRAxjmL7OIu8DA0CvBR/tXcwc8ruCAln"
    "IJLJ5W66jSmLXUhKWu31l3J2+6P+koRSjngVZqIuZKOyKJ1q6aawrSDQiE7SBZBnqjNJJ6"
    "pBpq3rMAF8euZ8mX50BOBCnl9IQlmBN8z2NqqhjwiLNlnMEtjMf9gX0/tgbvIRIvDD8zjc"
    "ga26BpaemyID1Zp0So+7G+PZs/Mf7sj98Z8NP4MBraxcRt7MYfTNgTiqRwuHh0EM4ctkSa"
    "gFGWaWIjHz8zsXnPY2L/18TGm0/zGghGyhm9XqDA5pGnM9pXKBB3SSmziW8hpwrcvrJoEs"
    "9nYklI+cFn2oP3t6O/bfvKSIz+4dbNoD+8MhD2KDebZdpDXx1G+Fwu1M/LLYn+w7rTD8rL"
    "Qu6GsaIFmlX+EoUkcKpqTZ/LmsuTehQoqw3vp9J8402Zwyo/ty7ab9uXb7rtS2Wid7KRvN"
    "3CtD8cK2RQpmcPmfoCgilyHx5RgJ2SRrREZS0CdmXUI07GQn2UjnaBb9zJTOI/eW2cV8lJ"
    "SaTpEgF63LQ42QOkglMhEbm+4db9tXVjm6sc2zxKUHktryhBHM11SLAz2EcWVUUzmCCs7w"
    "Jhk6+s+6u9kU0vY5yMQ7+Lx2bvh+8Jjs3eD5rYUrMXRoH+WtnvVSc04/L92rxvzF+uheu2"
    "G/Rw3XZtEweqfBfnUYwZcXYlWXA70lzTJB6ibBeOG4fDJNjqdBsgVFa1DLUuD9FHYfgogo"
    "o+pp5j1ucwUV60msxnyqoWpdblUdLQUQ0o/VJxt3tCDbyI1/SFWb8Cz6ly3BfQTc/40m8B"
    "e6PRba6s9frjAsfJoGcrwBqvMqLr0eIFhrgtQ0mmmmXeHVckK3ZP5r07wpCmU05P9Uvr/0"
    "hWzP07Hv66kW+145xmkYC6C7NiUos1p9tmNZTaHIe1l3y07XlY+6JG7Pj4N60QGZfDLBCt"
    "TqdRre1sqbWdYoGAq7EDxNj8MAFenJ83qbDn5/UVFnR5gGpFSXjFaPn7/WhY874gdSmAnH"
    "AV4EdMXXlqMBrKT68T6xaKEHWuzibwTgbWX0Wu17ejXnEuhD/o7bHiNiovq38BzLGoJA=="
)
