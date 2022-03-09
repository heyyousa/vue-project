import axios from 'axios'

const axiosHip = axios.create({
  baseURL: 'http://192.168.16.127:8000'
})

export default axiosHip