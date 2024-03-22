
import os
import subprocess


#pasta_atual = ''
pasta_atual = os.getcwd()
arquivos_ecmwf = os.listdir(pasta_atual)


print(arquivos_ecmwf)
arquivos_ecmwf2 = [arq for arq in arquivos_ecmwf if arq.endswith('.grib2') ]
print(arquivos_ecmwf2)
nome_novo = arquivos_ecmwf2[0].replace("grib2","nc")
resultado= f'plotar{nome_novo}'

#print('cdo -f nc copy' + arquivos_ecmwf2[0] + ' ' +resultado)
#subprocess.run(['cdo', 'copy', comando_1, resultado])
#cdo copy y1980.nc y1981.nc y1982.nc temp.1980.1982.nc


for arq_ec in arquivos_ecmwf2:
    nome_novo = arq_ec.replace("grib2","nc")
    resultado= f'plotar{nome_novo}'
    print('cdo -f nc copy' + arq_ec + ' ' +nome_novo)
    subprocess.run(['cdo', '-f', 'nc', 'copy', arq_ec, resultado])
