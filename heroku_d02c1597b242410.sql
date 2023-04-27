-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-04-2023 a las 07:33:56
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `heroku_d02c1597b242410`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usersbernal`
--

CREATE TABLE `usersbernal` (
  `idusers` int(10) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `datebirth` date NOT NULL,
  `placeOfBirth` varchar(100) NOT NULL,
  `userType` varchar(100) NOT NULL DEFAULT 'Regular',
  `firstName` varchar(100) NOT NULL,
  `lastName` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usersbernal`
--

INSERT INTO `usersbernal` (`idusers`, `username`, `password`, `email`, `datebirth`, `placeOfBirth`, `userType`, `firstName`, `lastName`) VALUES
(1, 'Bernal', 'bernal', 'bernal@mail.com', '1999-10-13', 'Mexico', 'Admin', 'Carlos', 'Bernal'),
(2, 'Chulises', 'UlisesNueva', 'ulises@mail.com', '2000-12-09', 'Mexico', 'Regular', 'Ulises', 'Vidal'),
(3, 'usereliminado', 'pass', 'eliminado@mail.com', '2000-12-09', 'Mexico', 'Regular', 'usuario', 'finiquitado');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `usersbernal`
--
ALTER TABLE `usersbernal`
  ADD PRIMARY KEY (`idusers`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `usersbernal`
--
ALTER TABLE `usersbernal`
  MODIFY `idusers` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
