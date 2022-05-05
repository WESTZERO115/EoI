#state파일에 변수저장 가능

output "tf101_image_id" {
  value = var.image_id
}

output "tf101_availability_zone_names" {
  value = var.availability_zone_names
}

output "tf101_admi_id_maps" {
  value = var.ami_id_maps
}

output "tf101_first_availability_zone_names" {
  value = var.availability_zone_names[0]
}
