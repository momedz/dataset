# ** Dataset detail  **


## URL
|                   |                                       |
| ----------------- | :-----------------------------------: |
| ** Method **      | GET                                   |
| ** Structure **   | /api/:version/                        |
| ** Example **     | /api/v1/                              |

## Header Params
    
|Key                  |Value                   |Required      |Description                                            |
| ------------------- | :--------------------: | :----------: | ----------                                            |
|X-Access             |String                  |true          |Username of the user who access this api               |

## Path Params

|Field Name  |Type          |Required      |Description              |
| ---------- | :----------: | :----------: | --------------------    |
| version    |String        |true          |version identifier       |

## Success Response
```json
{
  "local": {
      "caseNumber": [
          {
              "stat": {
                  "count": 14500,
                  "cluster": 7,
                  "dimention": 9
              },
              "name": "shuttle_9d"
          },
          {
              "stat": {
                  "count": 20000,
                  "cluster": 26,
                  "dimention": 16
              },
          "name": "letter_recognition_16d"
          }
      ],
      "synthetic": [
          {
              "stat": {
                  "count": 5000,
                  "cluster": 15,
                  "dimention": 2
              },
              "name": "s3_label"
          },
          {
              "stat": {
                  "count": 1000,
                  "cluster": 2,
                  "dimention": 3
              },
          "name": "chainlink_3d"
          }
      ],
    },
  "online": "TODO"
}
```

## Error Response
```json
{
  "code": 400,
  "error": {
    "code": 1,
    "message": "Missing header"
  }
}
```

## HTTP Status code

|Error Code   |Meaning                                                                                          |
| ----------- | :----------------------------------------------------------------------------------------------:|
|400          |	Bad Request – Missing header, wrong input data format, or case is not available to be assigned. |
|404          |	Not Found - The specified could not be found.                                                   |
|500          |	Internal Server Error – Something bad happens on the server/database.                           |
