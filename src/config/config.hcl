database {
  host = "localhost"
  port = 5432

  credentials {
    username = "admin"
    password = "secret"
  }
}

logging {
  level = "info"
  file = "app.log"
}

servers = [
  {
    name = "server1"
    ip   = "192.168.1.1"
  },
  {
    name = "server2"
    ip   = "192.168.1.2"
  }
]