from enum import Enum


class OrderStatus(Enum):
    PENDING = "Pending"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"


status = OrderStatus.SHIPPED

print("Current order status:", status.value)
