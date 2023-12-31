from __future__ import annotations

class G1Element:
    SIZE: ClassVar[int] = ...
    def __new__(cls) -> G1Element: ...
    def get_fingerprint(self) -> int: ...
    @staticmethod
    def from_bytes_unchecked(b: bytes) -> G1Element: ...
    def pair(self, other: G2Element) -> GTElement: ...
    @staticmethod
    def generator() -> G1Element: ...
    def __add__(self, other: G1Element) -> G1Element: ...
    def __iadd__(self, other: G1Element) -> None: ...
    def __init__(self) -> None: ...
    def __hash__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __richcmp__(self) -> Any: ...
    def __deepcopy__(self) -> G1Element: ...
    def __copy__(self) -> G1Element: ...
    @staticmethod
    def from_bytes(bytes) -> G1Element: ...
    @staticmethod
    def parse_rust(ReadableBuffer) -> Tuple[G1Element, int]: ...
    def to_bytes(self) -> bytes: ...
    def __bytes__(self) -> bytes: ...
    def get_hash(self) -> bytes32: ...
    def to_json_dict(self) -> Dict[str, Any]: ...
    @staticmethod
    def from_json_dict(o: Dict[str, Any]) -> G1Element: ...

class G2Element:
    SIZE: ClassVar[int] = ...
    def __new__(cls) -> G2Element: ...
    def get_fingerprint(self) -> int: ...
    @staticmethod
    def from_bytes_unchecked(b: bytes) -> G2Element: ...
    def pair(self, other: G1Element) -> GTElement: ...
    @staticmethod
    def generator() -> G2Element: ...
    def __hash__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __richcmp__(self) -> bool: ...
    def __deepcopy__(self) -> G2Element: ...
    def __copy__(self) -> G2Element: ...
    @staticmethod
    def from_bytes(bytes) -> G2Element: ...
    @staticmethod
    def parse_rust(ReadableBuffer) -> Tuple[G2Element, int]: ...
    def to_bytes(self) -> bytes: ...
    def __bytes__(self) -> bytes: ...
    def get_hash(self) -> bytes32: ...
    def to_json_dict(self) -> Dict[str, Any]: ...
    @staticmethod
    def from_json_dict(o: Dict[str, Any]) -> G2Element: ...

class GTElement:
    SIZE: ClassVar[int] = ...
    @staticmethod
    def from_bytes_unchecked(b: bytes) -> GTElement: ...
    def __mul__(self, rhs: GTElement) -> GTElement: ...
    def __imul__(self, rhs: GTElement) -> None: ...
    def __hash__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __richcmp__(self) -> bool: ...
    def __deepcopy__(self) -> GTElement: ...
    def __copy__(self) -> GTElement: ...
    @staticmethod
    def from_bytes(bytes) -> GTElement: ...
    @staticmethod
    def parse_rust(ReadableBuffer) -> Tuple[GTElement, int]: ...
    def to_bytes(self) -> bytes: ...
    def __bytes__(self) -> bytes: ...
    def get_hash(self) -> bytes32: ...
    def to_json_dict(self) -> Dict[str, Any]: ...
    @staticmethod
    def from_json_dict(o: Dict[str, Any]) -> GTElement: ...

class PrivateKey:
    PRIVATE_KEY_SIZE: ClassVar[int] = ...
    def sign_g2(self, msg: bytes, dst: bytes) -> G2Element: ...
    def get_g1(self) -> G1Element: ...
    def __hash__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __richcmp__(self) -> bool: ...
    def __deepcopy__(self) -> PrivateKey: ...
    def __copy__(self) -> PrivateKey: ...
    @staticmethod
    def from_bytes(bytes) -> PrivateKey: ...
    @staticmethod
    def parse_rust(ReadableBuffer) -> Tuple[PrivateKey, int]: ...
    def to_bytes(self) -> bytes: ...
    def __bytes__(self) -> bytes: ...
    def get_hash(self) -> bytes32: ...
    def to_json_dict(self) -> Dict[str, Any]: ...
    @staticmethod
    def from_json_dict(o: Dict[str, Any]) -> PrivateKey: ...

class AugSchemeMPL:
    @staticmethod
    def sign(pk: PrivateKey, msg: bytes, prepend_pk: G1Element = None) -> G2Element: ...
    @staticmethod
    def aggregate(sigs: Sequence[G2Element]) -> G2Element: ...
    @staticmethod
    def verify(pk: G1Element, msg: bytes, sig: G2Element) -> bool: ...
    @staticmethod
    def aggregate_verify(pks: Sequence[G1Element], msgs: Sequence[bytes], sig: G2Element) -> bool: ...
    @staticmethod
    def key_gen(seed: bytes) -> PrivateKey: ...
    @staticmethod
    def g2_from_message(msg: bytes) -> G2Element: ...
    @staticmethod
    def derive_child_sk(pk: PrivateKey, index: int) -> PrivateKey: ...
    @staticmethod
    def derive_child_sk_unhardened(pk: PrivateKey, index: int) -> PrivateKey: ...
