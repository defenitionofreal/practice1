from ..models import Nonce


def save_signed(data, pk=None) -> Nonce:
    return Nonce.objects.update(id=pk, signed_nonce=b'data')