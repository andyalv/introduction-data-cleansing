INSERT INTO clientes (id, edad, genero, fecha_registro)
SELECT
    cliente_id::int,
    NULLIF(edad, '')::float,
    NULLIF(genero, '')::text,
    NULLIF(fecha_registro, '')::date
FROM stage_clientes;

INSERT INTO visitas_mensuales (cliente_id, cuenta_visitas)
SELECT
    cliente_id::int,
    NULLIF(visitas_mensuales, '')::int
FROM stage_clientes;

INSERT INTO compra_restaurante (cliente_id, metodo_pago, monto_compra)
SELECT
    cliente_id::int,
    NULLIF(metodo_pago, '')::text,
    NULLIF(monto_compra, '')::float
FROM stage_clientes;