from pydantic import BaseModel

# Define a Pydantic model for venue details 
# (demonstrating Output as Pydantic)
class VenueDetails(BaseModel):
    venue: str
    address: str
    location: str
    capacity: int
    booking_status: str
    client_id: str
    
