CREATE TABLE IF NOT EXISTS clientes (
	id int PRIMARY KEY,
	edad int,
	genero text,
	fecha_registro date
);

CREATE TABLE IF NOT EXISTS visitas_mensuales (
	cliente_id int REFERENCES clientes(id),
	cuenta int
);

CREATE TABLE IF NOT EXISTS compra_restaurante (
	cliente_id int REFERENCES clientes(id),
	metodo_pago text,
	monto_compra float
);