from typing import List, Tuple

from .exceptions import MyException
from ..models import MarkingCode


def fetch_unprinted(x: int = 100) -> List[MarkingCode]:
    if x <= 100:
        items = MarkingCode.objects.all()[:x]
        for item in items:
            item.status = MarkingCode.STATUS_CHOICES[1][0]
        MarkingCode.objects.bulk_update(items, fields=['status'])
        return items
    else:
        raise MyException("Значение X превышает 100")


def mark_as_printed(items: list):
    if items:
        try:
            obj_list = MarkingCode.objects.filter(pk__in=items)
            for item in obj_list:
                item.status = MarkingCode.STATUS_CHOICES[7][0]
            MarkingCode.objects.bulk_update(obj_list, fields=['status'])
            return True, ""
        except Exception as e:
            return False, f"{e}"
    else:
        raise MyException("Список кодов пуст")


def scan_codes(list_of_scanned_codes: list):
    for code in list_of_scanned_codes:
        queryset = MarkingCode.objects.filter(value__in=code)
        if code == queryset:
            if queryset.SCANNED or queryset.ERROR or queryset.SUCCESSFULL:
                return 'already scanned'
            elif queryset.CONFIRMED:
                queryset.update(status=MarkingCode.SCANNED)
                return 'ok'
            else:
                return 'error'
        else:
            return 'not found'
