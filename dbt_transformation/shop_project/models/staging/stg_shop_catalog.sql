{{
    config(
        schema='staging'
    )
}}

WITH source AS (
    SELECT * FROM {{source('shop_raw', 'CATALOG')}}
),

renamed AS (
    SELECT
        PRODUCT_ID,
        TRIM(PRODUCT_NAME) AS PRODUCT_NAME,
        TRIM(CATEGORY) AS CATEGORY,
        BASE_PRICE
    FROM source
)

SELECT * FROM renamed