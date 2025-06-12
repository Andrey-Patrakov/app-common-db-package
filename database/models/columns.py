from sqlalchemy import func, true, false, DateTime
from datetime import datetime
from typing import Annotated
from sqlalchemy.orm import mapped_column


int_pk = Annotated[int, mapped_column(primary_key=True)]
str_uniq = Annotated[str, mapped_column(unique=True, nullable=False)]
str_not_null = Annotated[str, mapped_column(nullable=False)]
str_null = Annotated[str, mapped_column(nullable=True)]
bool_true = Annotated[bool, mapped_column(server_default=true())]
bool_false = Annotated[bool, mapped_column(server_default=false())]
created_at = Annotated[datetime, mapped_column(type_=DateTime(timezone=True), server_default=func.now())]  # noqa
datetime_null = Annotated[datetime, mapped_column(type_=DateTime(timezone=True), nullable=True)]  # noqa
