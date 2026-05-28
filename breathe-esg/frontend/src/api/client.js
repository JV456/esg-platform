import axios from "axios";

const apiClient = axios.create({
  baseURL: "https://breathe-esg-backend.onrender.com",
});

export default apiClient;