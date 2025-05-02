# Clase para validaciones
class Validatable:
  @staticmethod
  # Valida si todos los objetos son instancais de la clase especificada
  def _validate_instances(objects, expected_type, error_message):
    if not all(isinstance(obj, expected_type) for obj in objects):
      raise TypeError(error_message)