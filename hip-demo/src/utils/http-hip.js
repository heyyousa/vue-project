import axios from 'axios'

const axiosHip = axios.create({
  baseURL: 'http://192.168.31.53:8000'
})

export default axiosHip