# Actualización Automática de JSON - Smartphones MercadoLibre

Este repositorio contiene un sistema automatizado que actualiza diariamente un archivo JSON con datos de smartphones obtenidos de la API de MercadoLibre.

## 📋 Descripción

El sistema incluye:
- **Script Python** (`update_json.py`) que descarga y procesa datos de MercadoLibre
- **GitHub Actions** (`.github/workflows/update-json.yml`) que ejecuta el script diariamente
- **Archivo JSON** (`smarphone500json.json`) que se actualiza automáticamente

## 🚀 Características

- ✅ Actualización automática diaria a las 03:00 UTC
- ✅ Obtención de datos en tiempo real desde MercadoLibre
- ✅ Transformación de datos al formato requerido
- ✅ Commit automático con mensaje descriptivo
- ✅ Manejo de errores y logging detallado
- ✅ Ejecución manual disponible

## 📁 Estructura del Proyecto

```
├── .github/
│   └── workflows/
│       └── update-json.yml      # Configuración de GitHub Actions
├── update_json.py               # Script principal de actualización
├── requirements.txt             # Dependencias de Python
├── smarphone500json.json       # Archivo JSON actualizado (generado)
└── README.md                   # Este archivo
```

## 🔧 Configuración

### Requisitos
- Python 3.10+
- Repositorio de GitHub
- Permisos de escritura en el repositorio

### Instalación Local

1. Clona el repositorio:
```bash
git clone <tu-repositorio>
cd jsonalimentado
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecuta el script manualmente:
```bash
python update_json.py
```

## 📊 Formato de Datos

El archivo JSON generado contiene la siguiente estructura:

```json
{
  "last_updated": "2024-01-15T03:00:00.000000",
  "total_products": 50,
  "source": "MercadoLibre API",
  "products": [
    {
      "ProductId": "MLA123456789",
      "Product Desc": "Samsung Galaxy S23",
      "Discount Price": 899.99,
      "Currency": "ARS",
      "Image Url": "https://http2.mlstatic.com/...",
      "Promotion Url": "https://articulo.mercadolibre.com.ar/...",
      "Sales180Day": 15
    }
  ]
}
```

## ⚙️ GitHub Actions

El workflow se ejecuta automáticamente:
- **Frecuencia**: Diariamente a las 03:00 UTC
- **Trigger manual**: Disponible en la pestaña "Actions"
- **Permisos**: Requiere permisos de escritura para hacer commit

### Ejecución Manual

1. Ve a la pestaña "Actions" en tu repositorio
2. Selecciona "Actualizar JSON de Smartphones"
3. Haz clic en "Run workflow"

## 🔍 Monitoreo

Puedes monitorear las ejecuciones en:
- **GitHub Actions**: Pestaña "Actions" del repositorio
- **Logs**: Cada ejecución muestra logs detallados del proceso
- **Commits**: Los cambios se reflejan en el historial de commits

## 🛠️ Personalización

### Modificar la frecuencia de actualización

Edita el archivo `.github/workflows/update-json.yml`:

```yaml
on:
  schedule:
    - cron: '0 3 * * *'  # Cambia este valor según necesites
```

### Cambiar la consulta de búsqueda

Modifica la URL en `update_json.py`:

```python
url = "https://api.mercadolibre.com/sites/MLA/search?q=smartphone"
```

### Ajustar el formato de datos

Edita la función `transform_product_data()` en `update_json.py` para modificar los campos del JSON.

## 🐛 Solución de Problemas

### Error de permisos
- Asegúrate de que el repositorio tenga permisos de escritura habilitados
- Verifica que el token `GITHUB_TOKEN` tenga los permisos necesarios

### Error de API
- El script incluye manejo de errores para problemas de conectividad
- Los logs mostrarán detalles específicos del error

### Archivo no se actualiza
- Verifica que el workflow esté habilitado en la configuración del repositorio
- Revisa los logs de GitHub Actions para errores específicos

## 📝 Logs y Debugging

El script incluye logging detallado:
- ✅ Operaciones exitosas
- ⚠️ Advertencias (productos con errores)
- ❌ Errores críticos

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el repositorio
2. Crea una rama para tu feature
3. Haz commit de tus cambios
4. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.
