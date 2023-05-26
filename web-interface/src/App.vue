<template>
  <div>
    <!-- Input para inserir o termo de busca -->
    <input type="text" v-model="termoBusca" placeholder="Digite sua busca">
    
    <!-- Botão para realizar a busca -->
    <button @click="realizarBusca">Buscar</button>
    
    <!-- Lista de resultados -->
    <ul>
      <!-- Para cada resultado, exibir em um item da lista -->
      <li v-for="(resultado, index) in resultados" :key="index">
        <ul>
          <!-- Para cada valor do resultado, exibir em um subitem da lista -->
          <li v-for="valor in resultado" :key="valor">
            {{ valor }}
          </li>
        </ul>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      // Termo de busca inserido pelo usuário
      termoBusca: '',
      
      // Array para armazenar os resultados da busca
      resultados: []
    };
  },
  methods: {
    // Função assíncrona para realizar a busca
    async realizarBusca() {
      try {
        // Faz uma requisição POST para um servidor local, enviando o termo de busca
        const response = await axios.post('http://127.0.0.1:5000/buscar', {
          termo_busca: this.termoBusca
        });
        
        // Armazena os resultados retornados na variável 'resultados'
        this.resultados = response.data;
        
        // Exibe os resultados no console
        console.log(response.data);
      } catch (error) {
        // Trata erros que possam ocorrer durante a busca
        console.error('Erro ao realizar a busca:', error);
      }
    }
  }
};
</script>
