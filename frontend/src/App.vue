<template>
  <div id="app">
    <h1>Lista de tarefas</h1>
    <button @click="getTasks">Buscar dados do servidor</button>
    <hr />
    <input v-model="newTask" type="text" />
    <button @click="addTask">Adicionar</button>
    <ul>
      <li v-for="task in tasks" :key="task.id">{{ task.title }}</li>
    </ul>
  </div>
</template>

<script>
import axios from "axios"

export default {
  data() {
    return {
      newTask: "",
      tasks: [],
    }
  },
  mounted() {
    this.getTasks()
  },
  methods: {
    async addTask() {
      await axios.post("http://172.30.0.11:8000/api/tasks/", {
        title: this.newTask,
      })
      this.getTasks()
    },
    getTasks() {
      axios.get("http://172.30.0.11:8000/api/tasks/").then((res) => {
        this.tasks = res.data
      })
    },
  },
}
</script>

<style></style>
