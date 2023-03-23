SELECT
    p.transaction_date,
    SUM(p.amount * cr.exchange_rate_to_eur) AS amount_in_eur
FROM
    payments p
        JOIN
    currencies c ON p.currency = c.currency_id
        LEFT JOIN
    blacklist b ON p.user_id_sender = b.user_id AND p.transaction_date >= b.blacklist_start_date AND (p.transaction_date <= b.blacklist_end_date OR b.blacklist_end_date IS NULL)
        LEFT JOIN LATERAL (
        SELECT
            exchange_rate_to_eur
        FROM
            currency_rates
        WHERE
                currency_id = p.currency AND exchange_date <= p.transaction_date
        ORDER BY
            exchange_date DESC
        LIMIT 1
        ) cr ON TRUE
WHERE
    c.end_date IS NULL
  AND
    b.user_id IS NULL
GROUP BY
    p.transaction_date
ORDER BY
    p.transaction_date;