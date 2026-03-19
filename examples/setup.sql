\c sistema_escolar;

create table estudiante(
        matricula varchar(20), 
        nombre varchar(100) not null,
        id_carrera serial references carrera(id),
        primary key( matricula));

CREATE TABLE curso (
    id INT PRIMARY KEY,
    nombre VARCHAR(60) NOT NULL
);

create table carrera(
    id serial primary key,
    nombre varchar(60) not null
);

create table inscrito(
        matricula varchar(20),
        id int,
        primary key (matricula, id),
        foreign key (matricula) references estudiante (matricula),
        foreign key ( id ) references curso( id )
);

CREATE TABLE plan_estudios (
    id_carrera INT REFERENCES carrera(id),
    id_materia INT REFERENCES materias(id),
    PRIMARY KEY (id_carrera, id_materia)
);

INSERT INTO estudiante (matricula, nombre, id_carrera) VALUES
-- Generación 2024
('2024-001', 'Eustaquio Zenón', 1), ('2024-002', 'Petronila Higinia', 3), ('2024-003', 'Gumersindo Torcuato', 4),
('2024-004', 'Filomena Teodosia', 2), ('2024-005', 'Indalecio Casimiro', 5), ('2024-006', 'Escolástica Brígida', 6),
('2024-007', 'Pancracio Ladislao', 1), ('2024-008', 'Hermenegildo Praxedes', 3),
-- Generación 2025
('2025-001', 'Anacleto Agapito', 1), ('2025-002', 'Bernabé Trifón', 2), ('2025-003', 'Casilda Teófila', 3), ('2025-004', 'Dionisio Pelayo', 4),
('2025-005', 'Eulalia Custodia', 5), ('2025-006', 'Fructuoso Valeriano', 6), ('2025-007', 'Genoveva Marciana', 1), ('2025-008', 'Hilario Donato', 2),
('2025-009', 'Inocencio Gaudencio', 3), ('2025-010', 'Jacinta Plácida', 4), ('2025-011', 'Leoncio Robustiano', 5), ('2025-012', 'Maximino Serapio', 6),
('2025-013', 'Nicanor Primitivo', 1), ('2025-014', 'Olimpia Saturnina', 2), ('2025-015', 'Prudencio Tiburcio', 3), ('2025-016', 'Quintín Ursicio', 4),
('2025-017', 'Rudesindo Victorio', 5), ('2025-018', 'Severiano Zenobia', 6), ('2025-019', 'Telmo Bonifacio', 1), ('2025-020', 'Ursula Domitila', 2),
('2025-021', 'Viviana Eutropia', 3), ('2025-022', ' Wilfredo Galdino', 4), ('2025-023', 'Zenón Hipólito', 5), ('2025-024', 'Adelaida Isadora', 6),
('2025-025', 'Basilio Justo', 1),
-- Generación 2026
('2026-001', 'Cástulo Librado', 2), ('2026-002', 'Dorotea Melitón', 3), ('2026-003', 'Eutiquio Nicomedes', 4), ('2026-004', 'Faustino Onésimo', 5),
('2026-005', 'Gertrudis Policarpo', 6), ('2026-006', 'Honorato Quirino', 1), ('2026-007', 'Ifigenia Restituto', 2), ('2026-008', 'Jerónimo Secundino', 3),
('2026-009', 'Ladislada Toribia', 4), ('2026-010', 'Modesto Urbano', 5), ('2026-011', 'Nazario Venancio', 6), ('2026-012', 'Orosia Walfrido', 1),
('2026-013', 'Peregrino Zósimo', 2), ('2026-014', 'Amalio Brígida', 3), ('2026-015', 'Cipriano Donatila', 4), ('2026-016', 'Edelmira Florencio', 5),
('2026-017', 'Gorgonio Heliodora', 6), ('2026-018', 'Iluminada Jovita', 1), ('2026-019', 'Leocadia Macario', 2), ('2026-020', 'Nemesiio Olegario', 3),
('2026-021', 'Presentación Rufo', 4), ('2026-022', 'Sotero Teódula', 5), ('2026-023', 'Vigilio Zenais', 6), ('2026-024', 'Zoraida Alipio', 1),
('2026-025', 'Bonifacio Cleofé', 2);

INSERT INTO curso (id, nombre) VALUES
(101, 'Fundamentos de Alquimia Contemporánea'),
(102, 'Herbolaria y Pociones Ancestrales'),
(103, 'Criptografía de Sigilos Medievales'),
(104, 'Astronomía y Astrolabios'),
(105, 'Retórica y Sofística Avanzada'),
(106, 'Pilotaje de Aeronaves Pesadas (Propulsión Etérea)'),
(107, 'Cálculo de Variable Compleja y Entrelazamiento Mágico'),
(108, 'Tanatología Aplicada y Vida después de la Muerte'),
(109, 'Anatomía Comparada y Estructuras Biológicas'),
(110, 'Jurisprudencia y Leyes del Viaje en el Tiempo'),
(111, 'Cartografía de Constelaciones y Flujos Estelares'),
(112, 'Ensamblaje de Motores Aeroespaciales de Plasma Alquímico'),
(113, 'Teoría de Sistemas y Redes de Conciencia'),
(114, 'Inmunología y Defensa de la Esencia Vital');

INSERT INTO carrera (id, nombre) VALUES
(1, 'Ingeniería en Seguridad y Estructura de la Realidad'),
(2, 'Licenciatura en Navegación y Diplomacia Interestelar'),
(3, 'Grado en Medicina Alquímica y Botánica Avanzada'),
(4, 'Ingeniería Astrofísica (Aeroespacial)'),
(5, 'Ingeniería en Sistemas de Conciencia'),
(6, 'Ingeniería en Biomecánica Alquímica');

INSERT INTO plan_estudios (id_carrera, id_curso) VALUES
-- 1. Ingeniería en Seguridad y Estructura de la Realidad
(1, 101), (1, 103), (1, 107), (1, 110),
-- 2. Licenciatura en Navegación y Diplomacia Interestelar
(2, 104), (2, 105), (2, 106), (2, 111),
-- 3. Grado en Medicina Alquímica y Botánica Avanzada
(3, 101), (3, 102), (3, 109), (3, 114),
-- 4. Ingeniería Astrofísica (Aeroespacial)
(4, 104), (4, 106), (4, 107), (4, 112),
-- 5. Ingeniería en Sistemas de Conciencia
(5, 103), (5, 105), (5, 107), (5, 113),
-- 6. Ingeniería en Biomecánica Alquímica
(6, 101), (6, 102), (6, 107), (6, 108);

INSERT INTO inscrito (matricula, id)
SELECT matricula, id_curso
FROM (
    SELECT 
        e.matricula, 
        pe.id_curso,
        ROW_NUMBER() OVER(PARTITION BY e.matricula ORDER BY RANDOM()) as num_fila
    FROM estudiante e
    JOIN plan_estudios pe ON e.id_carrera = pe.id_carrera
) AS asignacion
WHERE num_fila <= 3; -- Asigna un máximo de 3 cursos por alumno