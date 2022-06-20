resource "aws_vpc" "tean" {
  cidr_block = "10.0.0.0/16"

}

resource "aws_subnet" "tean-public-1" {
  cidr_block        = "10.0.101.0/24"
  vpc_id            = aws_vpc.tean.id
  availability_zone = "us-east-1a"

}

resource "aws_subnet" "tean-public-2" {
  cidr_block        = "10.0.102.0/24"
  vpc_id            = aws_vpc.tean.id
  availability_zone = "us-east-1b"

}



resource "aws_subnet" "tean-private-1" {
  vpc_id                  = aws_vpc.tean.id
  cidr_block              = "10.0.10.0/24"
  map_public_ip_on_launch = "true"
  availability_zone       = "us-east-1a"

}

resource "aws_subnet" "tean-private-2" {
  vpc_id                  = aws_vpc.tean.id
  cidr_block              = "10.0.20.0/24"
  map_public_ip_on_launch = "true"
  availability_zone       = "us-east-1b"

}

resource "aws_internet_gateway" "tean" {
  vpc_id = aws_vpc.tean.id

}

resource "aws_route_table" "tean" {
  vpc_id = aws_vpc.tean.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.tean.id
  }
}

resource "aws_route_table_association" "tean-1" {
  subnet_id      = aws_subnet.tean-public-1.id
  route_table_id = aws_route_table.tean.id
}

resource "aws_route_table_association" "tean-2" {
  subnet_id      = aws_subnet.tean-public-2.id
  route_table_id = aws_route_table.tean.id
}

