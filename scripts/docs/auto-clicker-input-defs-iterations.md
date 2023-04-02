# iterations Schema

```txt
auto-clicker-input.schema.json#/$defs/iterations
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                          |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [auto-clicker-input.schema.json\*](../../out/auto-clicker-input.schema.json "open original schema") |

## iterations Type

`object` ([iterations](auto-clicker-input-defs-iterations.md))

# iterations Properties

| Property                      | Type      | Required | Nullable       | Defined by                                                                                                                                                     |
| :---------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [min](#min)                   | `integer` | Required | cannot be null | [Auto Clicker Input](auto-clicker-input-defs-iterations-properties-min.md "auto-clicker-input.schema.json#/$defs/iterations/properties/min")                   |
| [max](#max)                   | `integer` | Required | cannot be null | [Auto Clicker Input](auto-clicker-input-defs-iterations-properties-max.md "auto-clicker-input.schema.json#/$defs/iterations/properties/max")                   |
| [distribution](#distribution) | `string`  | Required | cannot be null | [Auto Clicker Input](auto-clicker-input-defs-iterations-properties-distribution.md "auto-clicker-input.schema.json#/$defs/iterations/properties/distribution") |

## min



`min`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-defs-iterations-properties-min.md "auto-clicker-input.schema.json#/$defs/iterations/properties/min")

### min Type

`integer`

## max



`max`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-defs-iterations-properties-max.md "auto-clicker-input.schema.json#/$defs/iterations/properties/max")

### max Type

`integer`

## distribution



`distribution`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-defs-iterations-properties-distribution.md "auto-clicker-input.schema.json#/$defs/iterations/properties/distribution")

### distribution Type

`string`

### distribution Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value      | Explanation |
| :--------- | :---------- |
| `"linear"` |             |
