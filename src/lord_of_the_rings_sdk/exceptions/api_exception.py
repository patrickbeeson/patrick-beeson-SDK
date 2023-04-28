class ApiException(Exception):
  """
  Custom exception to handle API errors.
  """

  def __init__(self, message):
    super().__init__(message)

  def __str__(self):
    return self.message