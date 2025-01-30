import json
import csv

class Dados:

    def __init__(self, dados):
        self.dados = dados
        self.nome_colunas = self.get_columns()
        self.qtd_linhas = self.size_data()


    def leitura_json(path):
        dados_json = []
        with open(path, 'r') as file:
            dados_json = json.load(file)
        return dados_json

    def leitura_csv(path):

        dados_csv = []
        with open(path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)

        return dados_csv

    @classmethod
    def leitura_dados(cls, path, tipo_dados):
        dados = []

        if tipo_dados == 'csv':
            dados = cls.leitura_csv(path)
        
        elif tipo_dados == 'json':
            dados = cls.leitura_json(path)

        return cls(dados)
    
    def get_columns(self):
        return list(self.dados[-1].keys())
    
    def rename_columns(Self, key_mapping):
        new_dados = []

        for old_dict in Self.dados:
            dict_temp = {}
            for old_key, value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value
            new_dados.append(dict_temp)

        Self.dados = new_dados
        Self.nome_colunas = Self.get_columns()

    def size_data(self):
        return len(self.dados)
    
    def join(dadosA, dadosB):
        combined_list = []
        combined_list.extend(dadosA.dados)
        combined_list.extend(dadosB.dados)
        
        return Dados(combined_list)
    

    def transformando_dados_tabela(self):
    
        dados_combinados_tabela = [self.nome_colunas]

        for row in self.dados:
            linha = []
            for coluna in self.nome_colunas:
                linha.append(row.get(coluna, 'Indisponivel'))
            dados_combinados_tabela.append(linha)
        
        return dados_combinados_tabela
    
    def salvando_dados(self, path):

        dados_combinados_tabela = self.transformando_dados_tabela()

        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(dados_combinados_tabela)