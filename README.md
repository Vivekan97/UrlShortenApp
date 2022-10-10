# UrlShortenApp
A full stack app with Angular frontend and Flask backend capable of shortening and retrieving full url.

## API Reference

#### Get Shortend Url

```http
  POST /api/short
```
| Request Body Example          |
| :-------------------          |
|   {   url: "your full url"   }|

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url` | `string` | **Required**. Your full url |

#### Get Full Url

```http
  POST /api/long
```

| Request Body Example          |
| :-------------------          |
|   {   url: "your short url"   }|

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `url`      | `string` | **Required**. Your short url |

#### get_shortened_url(full_url)

    Return the short url

#### get_long_url(short_url)

    Return the full retrieved url