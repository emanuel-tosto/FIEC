SELECT 
    IF(uf='CE','Ceara',IF(regiao_geografica='Nordeste','Nordeste','Brasil')) AS Localidade, 
    
    IF(uf='CE',(SELECT count(*) FROM atracacao_fato WHERE uf = 'CE'),IF(regiao_geografica='Nordeste',(SELECT count(*) FROM atracacao_fato WHERE regiao_geografica='Nordeste'),(SELECT count(*) FROM atracacao_fato)) AS Numero_Atracacoes_Por_Localidade,
    
    AVG(T_espera_atracacao) AS tempo_espera_medio, 
    
    AVG(T_atracado) AS tempo_atracado_medio,
    
    mes,
    
    ano


FROM atracacao_fato

WHERE (ano=2018 OR ano=2019)
GROUP BY localidade,mes,ano;