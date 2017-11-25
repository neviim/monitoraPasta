#!/usr/bin/env python3
# -*-coding: utf-8-*-
# Neviim - 2017
import shutil
import time
import os


class MonitoraPasta(object):
    """docstring para MonitoraPasta.
        Parametros:
            drOrigem  = Diretorio de origem.
            drDestino = Diretorio destino onde sera movido o aquivo.

            - Caso não seja informado sera adota ../data/dr<1/2> por padrão.

            Uso:
                monitoraPasta = MonitoraPasta(drOrigem, drDestino)
    """
    def __init__(self, drOrigem="../data/dr1", drDestino="../data/dr2"):
        super(MonitoraPasta, self).__init__()
        self.drOrigem  = drOrigem
        self.drDestino = drDestino
        self.tempo = 1
        self.nome = "output_"
        self.extensao = ".txt"
        # funcao lambda idn
        self.novoNome = lambda idn: self.drDestino+"/"+self.nome+str(idn)+self.extensao

    def tem_arquivo(self):
        """ havendo arquivo na pasta Origem, ele sera processado.
                Uso:
                    monitoraPasta.tem_arquivo()
        """
        listArquivos = os.listdir(self.drOrigem)

        # caso haja arquivo no diretorio origem.
        if len(listArquivos) > 0:
            for arquivo in listArquivos:
                arquivoOriguem = self.drOrigem+"/"+arquivo

                # aqui: chama metodo de processara o arquivo.
                # ha ser desenvolvido...
                # -------------------------------------------

                # remomeia o arquivo, idn não sera repetido.
                idn = 1; arquivoRenomeado = self.novoNome(idn)
                while os.path.exists(arquivoRenomeado):
                    idn = idn+1; arquivoRenomeado = self.novoNome(idn)

                # o arquivo é novido ao drDestino.
                shutil.move(arquivoOriguem, arquivoRenomeado)
                print("Aquivo: "+arquivo+" processado.")
        return


if __name__ == "__main__":
    # path dos diretorios origem e destino
    dr1 = "../data/dr1" # origem
    dr2 = "../data/dr2" # destino
    tempo = 1 # tempo de espera em segundos

    # ativa classe de monitoramento de fasta.
    monitorandoPasta = MonitoraPasta(dr1, dr2)

    # loop infinito.
    print("Monitoramento inicializado, (CTRL+C) para cancelar.")

    while True:
        monitorandoPasta.tem_arquivo()
        time.sleep(tempo)
