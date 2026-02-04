class AppError(Exception):
    code = "Internal_Error"
    status_code = 500
    
class InvalidCEPError(AppError):
    code = "Invalid_CEP_Error"
    status_code = 400

class ExternalAPIError(AppError):
    code = "External_API_Error"
    status_code = 503