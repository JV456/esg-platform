import axios from "axios";

const apiClient = axios.create({
  baseURL: "https://YOUR-BACKEND-URL/api",
});

export default apiClient;