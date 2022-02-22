# vcoml

Imagine a markup language, but worse

## Syntax Example

VcoML:

```vcoml
:"members"
  :297045071457681409
    :"username"
      "vcokltfre"
    :"discriminator"
      6868
    :"mfa"
      ya
    :"verified"
      na
    :"email"
      idk
    :"roles"
      >
        :"id"
          1234
        :"name"
          "Admin"
      >
        :"id"
          5678
        :"name"
          "Moderator"
```

YAML:

```yml
members:
  297045071457681409:
    username: vcokltfre
    discriminator: 6868
    mfa: true
    verified: false
    email: null
    roles:
      - id: 1234
        name: Admin
      - id: 5678
        name: Moderator
```

## Usage

```py
from vcoml import unpack


data = unpack("""
:"abc"
  123
:"def"
  >
    "list"
  >
    "more list"
""")

print(data)
```

## Todo

- Implement packing
- CLI
