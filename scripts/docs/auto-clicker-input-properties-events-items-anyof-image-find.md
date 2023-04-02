# Image Find Schema

```txt
auto-clicker-input.schema.json#/properties/children/items/anyOf/4
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                          |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [auto-clicker-input.schema.json\*](../../out/auto-clicker-input.schema.json "open original schema") |

## 4 Type

`object` ([Image Find](auto-clicker-input-properties-events-items-anyof-image-find.md))

# 4 Properties

| Property                               | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                       |
| :------------------------------------- | :------------ | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [notes](#notes)                        | `string`      | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-image-find-properties-notes.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/4/properties/notes")                       |
| [type](#type)                          | Not specified | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-image-find-properties-type.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/4/properties/type")                         |
| [image\_path](#image_path)             | `string`      | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-image-find-properties-image_path.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/4/properties/image_path")             |
| [confidence](#confidence)              | `number`      | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-image-find-properties-confidence.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/4/properties/confidence")             |
| [grayscale](#grayscale)                | `boolean`     | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-image-find-properties-grayscale.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/4/properties/grayscale")               |
| [region](#region)                      | `array`       | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-defs-region.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/4/properties/region")                                                                    |
| [attempts](#attempts)                  | `integer`     | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-image-find-properties-attempts.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/4/properties/attempts")                 |
| [execution\_modulo](#execution_modulo) | `integer`     | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-image-find-properties-execution_modulo.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/4/properties/execution_modulo") |
| [iterations](#iterations)              | `object`      | Required | cannot be null | [Auto Clicker Input](auto-clicker-input-defs-iterations.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/4/properties/iterations")                                                            |

## notes



`notes`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-image-find-properties-notes.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/4/properties/notes")

### notes Type

`string`

## type



`type`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-image-find-properties-type.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/4/properties/type")

### type Type

unknown

### type Constraints

**constant**: the value of this property must be equal to:

```json
"IMAGE_FIND"
```

## image\_path



`image_path`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-image-find-properties-image_path.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/4/properties/image_path")

### image\_path Type

`string`

## confidence



`confidence`

*   is optional

*   Type: `number`

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-image-find-properties-confidence.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/4/properties/confidence")

### confidence Type

`number`

## grayscale



`grayscale`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-image-find-properties-grayscale.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/4/properties/grayscale")

### grayscale Type

`boolean`

## region



`region`

*   is optional

*   Type: `array` ([region](auto-clicker-input-defs-region.md))

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-defs-region.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/4/properties/region")

### region Type

`array` ([region](auto-clicker-input-defs-region.md))

## attempts



`attempts`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-image-find-properties-attempts.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/4/properties/attempts")

### attempts Type

`integer`

## execution\_modulo



`execution_modulo`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-image-find-properties-execution_modulo.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/4/properties/execution_modulo")

### execution\_modulo Type

`integer`

## iterations



`iterations`

*   is required

*   Type: `object` ([iterations](auto-clicker-input-defs-iterations.md))

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-defs-iterations.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/4/properties/iterations")

### iterations Type

`object` ([iterations](auto-clicker-input-defs-iterations.md))
