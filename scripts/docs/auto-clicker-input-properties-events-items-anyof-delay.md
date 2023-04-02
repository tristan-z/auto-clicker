# Delay Schema

```txt
auto-clicker-input.schema.json#/properties/children/items/anyOf/1
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                          |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [auto-clicker-input.schema.json\*](../../out/auto-clicker-input.schema.json "open original schema") |

## 1 Type

`object` ([Delay](auto-clicker-input-properties-events-items-anyof-delay.md))

# 1 Properties

| Property                               | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                  |
| :------------------------------------- | :------------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [notes](#notes)                        | `string`      | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-delay-properties-notes.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/1/properties/notes")                       |
| [type](#type)                          | Not specified | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-delay-properties-type.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/1/properties/type")                         |
| [delay\_time](#delay_time)             | `integer`     | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-delay-properties-delay_time.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/1/properties/delay_time")             |
| [time\_offset](#time_offset)           | `integer`     | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-delay-properties-time_offset.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/1/properties/time_offset")           |
| [execution\_modulo](#execution_modulo) | `integer`     | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-delay-properties-execution_modulo.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/1/properties/execution_modulo") |
| [iterations](#iterations)              | `object`      | Required | cannot be null | [Auto Clicker Input](auto-clicker-input-defs-iterations.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/1/properties/iterations")                                                       |

## notes



`notes`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-delay-properties-notes.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/1/properties/notes")

### notes Type

`string`

## type



`type`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-delay-properties-type.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/1/properties/type")

### type Type

unknown

### type Constraints

**constant**: the value of this property must be equal to:

```json
"DELAY"
```

## delay\_time



`delay_time`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-delay-properties-delay_time.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/1/properties/delay_time")

### delay\_time Type

`integer`

## time\_offset



`time_offset`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-delay-properties-time_offset.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/1/properties/time_offset")

### time\_offset Type

`integer`

## execution\_modulo



`execution_modulo`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-delay-properties-execution_modulo.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/1/properties/execution_modulo")

### execution\_modulo Type

`integer`

## iterations



`iterations`

*   is required

*   Type: `object` ([iterations](auto-clicker-input-defs-iterations.md))

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-defs-iterations.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/1/properties/iterations")

### iterations Type

`object` ([iterations](auto-clicker-input-defs-iterations.md))
