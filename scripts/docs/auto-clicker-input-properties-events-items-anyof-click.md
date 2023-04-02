# Click Schema

```txt
auto-clicker-input.schema.json#/properties/children/items/anyOf/0
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                          |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [auto-clicker-input.schema.json\*](../../out/auto-clicker-input.schema.json "open original schema") |

## 0 Type

`object` ([Click](auto-clicker-input-properties-events-items-anyof-click.md))

# 0 Properties

| Property                               | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                  |
| :------------------------------------- | :------------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [notes](#notes)                        | `string`      | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-click-properties-notes.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/0/properties/notes")                       |
| [type](#type)                          | Not specified | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-click-properties-type.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/0/properties/type")                         |
| [click\_type](#click_type)             | `string`      | Required | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-click-properties-click_type.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/0/properties/click_type")             |
| [pixel\_offset](#pixel_offset)         | `integer`     | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-click-properties-pixel_offset.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/0/properties/pixel_offset")         |
| [coords](#coords)                      | `array`       | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-click-properties-coords.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/0/properties/coords")                     |
| [execution\_modulo](#execution_modulo) | `integer`     | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-click-properties-execution_modulo.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/0/properties/execution_modulo") |
| [iterations](#iterations)              | `object`      | Required | cannot be null | [Auto Clicker Input](auto-clicker-input-defs-iterations.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/0/properties/iterations")                                                       |

## notes



`notes`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-click-properties-notes.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/0/properties/notes")

### notes Type

`string`

## type



`type`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-click-properties-type.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/0/properties/type")

### type Type

unknown

### type Constraints

**constant**: the value of this property must be equal to:

```json
"CLICK"
```

## click\_type



`click_type`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-click-properties-click_type.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/0/properties/click_type")

### click\_type Type

`string`

### click\_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value     | Explanation |
| :-------- | :---------- |
| `"left"`  |             |
| `"right"` |             |

## pixel\_offset



`pixel_offset`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-click-properties-pixel_offset.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/0/properties/pixel_offset")

### pixel\_offset Type

`integer`

## coords



`coords`

*   is optional

*   Type: `array` ([coords](auto-clicker-input-properties-events-items-anyof-click-properties-coords.md))

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-click-properties-coords.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/0/properties/coords")

### coords Type

`array` ([coords](auto-clicker-input-properties-events-items-anyof-click-properties-coords.md))

## execution\_modulo



`execution_modulo`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-click-properties-execution_modulo.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/0/properties/execution_modulo")

### execution\_modulo Type

`integer`

## iterations



`iterations`

*   is required

*   Type: `object` ([iterations](auto-clicker-input-defs-iterations.md))

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-defs-iterations.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/0/properties/iterations")

### iterations Type

`object` ([iterations](auto-clicker-input-defs-iterations.md))
