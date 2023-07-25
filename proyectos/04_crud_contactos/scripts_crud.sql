
-- SCRIPTS PARA PROBAR CRUD - CONTACTOS --

-- *************************************** --
-- CREAR CONTACTO --
C
-- EJECUCUÓN --
EXEC [dbo].[pa_CrearContacto_basico] 'John', 'Doe', '1234567890', 'john.doe@example.com'
-- *************************************** --






-- *************************************** --
-- ACTUALIZAR CONTACTO
ALTER PROC [dbo].[pa_ActualizarContacto_basico]
@ID int,
@nombre varchar(50),
@apellido varchar(50),
@telefono varchar(10),
@correo varchar(20)
AS
BEGIN
IF EXISTS (SELECT TOP 1 ID FROM Contacto WHERE Contacto.ID = @ID)
	BEGIN
		UPDATE [dbo].[Contacto]
		   SET	[Nombre] = @nombre,
				[Apellido] =@apellido,
				[Telefono] = @telefono,
				[Correo] = @correo
		WHERE 	Contacto.ID = @ID
		-- Mensaje de éxito
			PRINT 'El contacto se actualizó correctamente.'
	END
	ELSE
		BEGIN
			SELECT 'El contacto no existe.'
			-- Mensaje de error si el contacto no existe
			PRINT 'El contacto no existe.'
		END
END
-- EJECUCUÓN --
EXEC [dbo].[pa_ActualizarContacto_basico] @ID = 3, @nombre = 'NuevoNombre', @apellido = 'NuevoApellido', @telefono = '1234567890', @correo = 'nuevo@example.com'
-- *************************************** --



-- *************************************** --
-- ELIMINAR CONTACTO
ALTER PROCEDURE [dbo].[pa_EliminarContacto_basico]
	@ID int
AS
BEGIN
	BEGIN TRY
		-- Validar parámetro ID
		IF @ID <= 0
		BEGIN
			RAISERROR('El ID del contacto debe ser mayor que cero.', 16, 1)
			RETURN
		END

		-- Verificar si el contacto existe
		IF EXISTS (SELECT 1 FROM [dbo].[Contacto] WHERE ID = @ID)
		BEGIN
			-- Eliminar el contacto
			DELETE FROM [dbo].[Contacto] WHERE ID = @ID
			
			-- Mensaje de éxito
			PRINT 'El contacto se eliminó correctamente.'
		END
		ELSE
		BEGIN
			-- Mensaje de error si el contacto no existe
			PRINT 'El contacto no existe.'
		END
	END TRY
	BEGIN CATCH
		-- Manejo de errores
		PRINT ERROR_MESSAGE()
	END CATCH
END
-- EJECUCUÓN --
EXEC [dbo].[pa_EliminarContacto_basico] @ID = 3
-- *************************************** --






-- *************************************** --
-- CONSULTAR TODOS
ALTER PROCEDURE [dbo].[pa_ConsultarContactos_basico]
AS
BEGIN
	BEGIN TRY
		-- Consultar todos los contactos
		SELECT [ID], [Nombre], [Apellido], [Telefono], [Correo]
		FROM [dbo].[Contacto]
	END TRY
	BEGIN CATCH
		-- Manejo de errores
		PRINT ERROR_MESSAGE()
	END CATCH
END
-- EJECUCUÓN --
EXEC [dbo].[pa_ConsultarContactos_basico]
-- *************************************** --

