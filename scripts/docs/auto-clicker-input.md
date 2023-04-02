# Auto Clicker Input Schema

```txt
auto-clicker-input.schema.json
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                        |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [auto-clicker-input.schema.json](../../out/auto-clicker-input.schema.json "open original schema") |

## Auto Clicker Input Type

`object` ([Auto Clicker Input](auto-clicker-input.md))

# Auto Clicker Input Properties

| Property                  | Type     | Required | Nullable       | Defined by                                                                                                          |
| :------------------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------ |
| [notes](#notes)           | `string` | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-notes.md "auto-clicker-input.schema.json#/properties/notes")     |
| [children](#children)     | `array`  | Required | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events.md "auto-clicker-input.schema.json#/properties/children") |
| [iterations](#iterations) | `object` | Required | cannot be null | [Auto Clicker Input](auto-clicker-input-defs-iterations.md "auto-clicker-input.schema.json#/properties/iterations") |

## notes



`notes`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-notes.md "auto-clicker-input.schema.json#/properties/notes")

### notes Type

`string`

## children



`children`

*   is required

*   Type: an array of merged types ([Details](auto-clicker-input-properties-events-items.md))

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events.md "auto-clicker-input.schema.json#/properties/children")

### children Type

an array of merged types ([Details](auto-clicker-input-properties-events-items.md))

## iterations



`iterations`

*   is required

*   Type: `object` ([iterations](auto-clicker-input-defs-iterations.md))

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-defs-iterations.md "auto-clicker-input.schema.json#/properties/iterations")

### iterations Type

`object` ([iterations](auto-clicker-input-defs-iterations.md))

# Auto Clicker Input Definitions

## Definitions group notes

Reference this group by using

```json
{"$ref":"auto-clicker-input.schema.json#/$defs/notes"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group execution\_modulo

Reference this group by using

```json
{"$ref":"auto-clicker-input.schema.json#/$defs/execution_modulo"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group click\_type

Reference this group by using

```json
{"$ref":"auto-clicker-input.schema.json#/$defs/click_type"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group iterations

Reference this group by using

```json
{"$ref":"auto-clicker-input.schema.json#/$defs/iterations"}
```

| Property                      | Type      | Required | Nullable       | Defined by                                                                                                                                                     |
| :---------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [min](#min)                   | `integer` | Required | cannot be null | [Auto Clicker Input](auto-clicker-input-defs-iterations-properties-min.md "auto-clicker-input.schema.json#/$defs/iterations/properties/min")                   |
| [max](#max)                   | `integer` | Required | cannot be null | [Auto Clicker Input](auto-clicker-input-defs-iterations-properties-max.md "auto-clicker-input.schema.json#/$defs/iterations/properties/max")                   |
| [distribution](#distribution) | `string`  | Required | cannot be null | [Auto Clicker Input](auto-clicker-input-defs-iterations-properties-distribution.md "auto-clicker-input.schema.json#/$defs/iterations/properties/distribution") |

### min



`min`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-defs-iterations-properties-min.md "auto-clicker-input.schema.json#/$defs/iterations/properties/min")

#### min Type

`integer`

### max



`max`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-defs-iterations-properties-max.md "auto-clicker-input.schema.json#/$defs/iterations/properties/max")

#### max Type

`integer`

### distribution



`distribution`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-defs-iterations-properties-distribution.md "auto-clicker-input.schema.json#/$defs/iterations/properties/distribution")

#### distribution Type

`string`

#### distribution Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value      | Explanation |
| :--------- | :---------- |
| `"linear"` |             |

## Definitions group region

Reference this group by using

```json
{"$ref":"auto-clicker-input.schema.json#/$defs/region"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |
