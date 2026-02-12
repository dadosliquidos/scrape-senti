use data_warehouse;

insert into data_warehouse.dim_sentimento(id_sentimentos,sentimento) values (3,'Neutro');
insert into data_warehouse.dim_sentimento(id_sentimentos,sentimento) values (0,'Negativo');
insert into data_warehouse.dim_sentimento(id_sentimentos,sentimento) values (1,'Positivo');
insert into data_warehouse.dim_sentimento(id_sentimentos,sentimento) values (4,'outros');



INSERT INTO dim_calendario (id_data, mes, ano)
WITH RECURSIVE gerador_datas AS (
    -- Data inicial
    SELECT '2025-01-01' AS data_atual
    UNION ALL
    -- Adiciona 1 dia até chegar ao final de 2026
    SELECT data_atual + INTERVAL 1 DAY
    FROM gerador_datas
    WHERE data_atual < '2026-12-31'
)
SELECT 
    data_atual AS id_data,
    -- Garante que o mês venha escrito em Português
    CASE MONTH(data_atual)
        WHEN 1 THEN 'Janeiro'
        WHEN 2 THEN 'Fevereiro'
        WHEN 3 THEN 'Março'
        WHEN 4 THEN 'Abril'
        WHEN 5 THEN 'Maio'
        WHEN 6 THEN 'Junho'
        WHEN 7 THEN 'Julho'
        WHEN 8 THEN 'Agosto'
        WHEN 9 THEN 'Setembro'
        WHEN 10 THEN 'Outubro'
        WHEN 11 THEN 'Novembro'
        WHEN 12 THEN 'Dezembro'
    END AS mes,
    CAST(YEAR(data_atual) AS CHAR) AS ano
FROM gerador_datas;

commit;