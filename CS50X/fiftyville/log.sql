-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Get information of tables of the database.
.schema tables

-- Get information about all tables.
.schema

-- Get some information about the theft.
SELECT description FROM crime_scene_reports WHERE year = 2024 AND month = 7 AND day = 28 AND street = 'Humphrey Street';

-- Look at the transcripts that mention the bakery and note all important information.
SELECT transcript, name FROM interviews WHERE year = 2024 AND day = 28 AND month = 7;



-- I- Name of the theif:

-- Get the name of the thief by targeting all parameters (person.id, person.phone_number, person.passport_number and person.license_plate).
-- The thief is the one who satisfies all the targeted conditions:
-- 1. Their ID is among IDs of people who used the ATM on Leggett Street the day of the theft (witness: Eugene).
-- 2. Their phone number is among the phone numbers of all callers whose calls had a duration of less than 60 seconds and were made on the day of the theft (witness: Raymond).
-- 3. Their passport number is among passport numbers of passengers that took the earliest flight on July 29, 2024, from Fiftyville (witness: Raymond).
-- 4. The license plate of their car is among the recorded license plates with exit activity within 10 minutes after the theft (witness: Ruth).


-- Target IDs of persons who have a bank account and used the ATM on Legget Street on the date of the theft (witness: Eugene).
-- With the atm_transaction table, we can get the account numbers of persons who used the ATM on Leggett Street on the date of the theft.
-- Account numbers stored in atm_transactions table are also stored in bank_accounts table (while bank_accounts contain account numbers of all people). And, while bank_accounts table store id of persons that
-- are stored in people table (people.id) we can target all IDs of persons that used the ATM on Legget Street on the date of the theft (witness: Eugene).
SELECT name
FROM people
WHERE id IN (
    SELECT person_id
    FROM bank_accounts
    WHERE account_number IN (
        SELECT account_number
        FROM atm_transactions
        WHERE year = 2024
          AND month = 7
          AND day = 28
          AND atm_location = 'Leggett Street'
          AND creation_year <= 2024
    )
)
-- Target all phone numbers of callers who made calls on the day of the theft with a duration of less than 60 seconds (witness: Raymond).
AND (
    phone_number IN (
        SELECT caller
        FROM phone_calls
        WHERE day = 28
          AND year = 2024
          AND month = 7
          AND duration < 60
    )
)
-- Target passport numbers of passengers who took the earliest flight the day after the theft from Fiftyville (witness: Raymond).
-- Used the MIN() function to target the minimum value of hour and minimum value of minute.
AND passport_number IN (
    SELECT passport_number
    FROM passengers
    WHERE flight_id IN (
        SELECT id
        FROM flights
        WHERE day = 29
          AND year = 2024
          AND month = 7
          AND hour = (
              SELECT MIN(hour)
              FROM flights
              WHERE day = 29
                AND year = 2024
                AND month = 7
                AND origin_airport_id = (
                    SELECT id
                    FROM airports
                    WHERE city = 'Fiftyville'
                )
          )
          AND minute = (
              SELECT MIN(minute)
              FROM flights
              WHERE day = 29
                AND year = 2024
                AND month = 7
                AND origin_airport_id = (
                    SELECT id
                    FROM airports
                    WHERE city = 'Fiftyville'
                )
                AND hour = (
                    SELECT MIN(hour)
                    FROM flights
                    WHERE day = 29
                      AND year = 2024
                      AND month = 7
                      AND origin_airport_id = (
                          SELECT id
                          FROM airports
                          WHERE city = 'Fiftyville'
                      )
                )
          )
          AND origin_airport_id = (
              SELECT id
              FROM airports
              WHERE city = 'Fiftyville'
          )
    )
)


-- Target all license plates of cars that exited the bakery within a time frame of 10 minutes. I used a time frame of more than 15 minutes after the theft, which occurred at 10:15,
-- and less than 30 minutes. Ruth mentioned: "Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away". Targeting 15 minutes after the theft is reasonable.
AND license_plate IN (
    SELECT license_plate
    FROM bakery_security_logs
    WHERE year = 2024
      AND month = 7
      AND day = 28
      AND hour = 10
      AND minute > 15
      AND minute < 30
      AND activity = 'exit'
);



-- II- City of Escape:
-- Get the name of the city the thief escaped to.
-- Target the earliest flight on July 29, 2024 where the origin airport is Fiftyville (witness: Raymond).
SELECT city
FROM airports
WHERE id = (
    SELECT destination_airport_id
    FROM flights
    WHERE origin_airport_id = (
        SELECT id
        FROM airports
        WHERE city = 'Fiftyville'
    )
    AND day = 29
    AND year = 2024
    AND month = 7
    AND hour = (
        SELECT MIN(hour)
        FROM flights
        WHERE day = 29
        AND year = 2024
        AND month = 7
        AND origin_airport_id = (
            SELECT id
            FROM airports
            WHERE city = 'Fiftyville'
        )
    )
    AND minute = (
        SELECT MIN(minute)
        FROM flights
        WHERE day = 29
        AND year = 2024
        AND month = 7
        AND origin_airport_id = (
            SELECT id
            FROM airports
            WHERE city = 'Fiftyville'
        )
        AND hour = (
            SELECT MIN(hour)
            FROM flights
            WHERE day = 29
            AND year = 2024
            AND month = 7
            AND origin_airport_id = (
                SELECT id
                FROM airports
                WHERE city = 'Fiftyville'
            )
        )
    )
);


-- III- Name of the accomplice:
-- Get the name of the accomplice who helped them escape.
-- Knowing that the thief is Bruce, the accomplice must be the one who was on a call with Bruce at the time of the theft while Raymond (the witness) heard the conversation.

SELECT name
FROM people
WHERE (
    phone_number = (
        SELECT receiver
        FROM phone_calls
        WHERE caller = (
            SELECT phone_number
            FROM people
            WHERE name = 'Bruce'
        )
        AND day = 28
        AND year = 2024
        AND month = 7
        AND duration < 60
    )
);
