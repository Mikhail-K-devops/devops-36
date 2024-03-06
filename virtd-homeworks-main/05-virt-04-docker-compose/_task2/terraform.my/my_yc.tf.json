# Указываем версию Terraform
terraform {
  required_version = ">= 0.12"
}
# Указываем провайдер и его версию
provider "yandex" {
  version = "~> 0.41"
  # Идентификатор облака
  cloud_id = var.cloud_id

  # Идентификатор каталога
  folder_id = var.folder_id

  # Токен для аутентификации
  token = var.token
}

# Определение переменных
variable "cloud_id" {
  description = "Идентификатор облака"
}

variable "folder_id" {
  description = "Идентификатор каталога"
}

variable "token" {
  description = "Токен для аутентификации"
}

# Создание виртуальной машины
resource "yandex_compute_instance" "vm" {
  name = "terraform-instance"

  # Используемые ресурсы
  resources {
    cores  = 2
    memory = 2
  }

  # Диск
  boot_disk {
    initialize_params {
      image_id = "fd8vmcue78qkj72h3v8t"
    }
  }

  # Сетевые интерфейсы
  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }

  # Метаданные
  metadata = {
    ssh-keys = "ubuntu:${file("~/.ssh/id_rsa.pub")}"
  }
}

# Создание сети
resource "yandex_vpc_network" "network-1" {
  name = "terraform-network"
}

# Создание подсети
resource "yandex_vpc_subnet" "subnet-1" {
  name           = "terraform-subnet"
  zone           = "ru-central1-a"
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["192.168.10.0/24"]
}
