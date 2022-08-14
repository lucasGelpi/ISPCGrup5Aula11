-- 1

CREATE TABLE Perro
(ID_Perro integer primary key not null,
Nombre varchar(30),
Fecha_nac date,
Sexo varchar(10),
DNI_Dueno integer not null,
foreign key (DNI_Dueno) references Dueno(DNI)
);

-- 2

insert into Perro values (6, 'CHOPER', '2021-5-13',
'MACHO', 15734093);

-- 12

select nombre, sexo from Perro where sexo = "MACHO" and fecha_nac between '2020-01-01' and '2022-12-31'
  



