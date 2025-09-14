#!/usr/bin/env python3
"""
Script para actualizar automáticamente el archivo JSON con datos de smartphones de MercadoLibre.
Este script se ejecuta diariamente via GitHub Actions para mantener actualizados los datos.
"""

import json
import requests
import sys
from datetime import datetime
from typing import Dict, List, Any


def fetch_mercadolibre_data(category: str, query: str) -> Dict[str, Any]:
    """
    Obtiene datos de una categoría específica desde la API de MercadoLibre.
    
    Args:
        category: Nombre de la categoría (para logging)
        query: Término de búsqueda para la API
        
    Returns:
        Dict con los datos de la API de MercadoLibre
    """
    url = f"https://api.mercadolibre.com/sites/MLA/search?q={query}&limit=50"
    
    # Headers para simular un navegador real
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'application/json',
        'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    try:
        print(f"Descargando datos de {category}...")
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        data = response.json()
        print(f"✅ {category}: {len(data.get('results', []))} productos obtenidos")
        return data
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error al obtener datos de {category}: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Error al decodificar JSON de {category}: {e}")
        return None


def fetch_all_categories() -> List[Dict[str, Any]]:
    """
    Obtiene datos de todas las categorías de productos.
    
    Returns:
        Lista de productos de todas las categorías combinados
    """
    categories = [
        ("Smartphones", "smartphone"),
        ("Tablets", "tablet"),
        ("Smartwatches", "smartwatch"),
        ("Portátiles", "laptop")
    ]
    
    all_products = []
    
    for category_name, query in categories:
        data = fetch_mercadolibre_data(category_name, query)
        
        if data and data.get("results"):
            products = data.get("results", [])
            # Agregar información de categoría a cada producto
            for product in products:
                product["category"] = category_name
            all_products.extend(products)
        else:
            print(f"⚠️  No se pudieron obtener datos de {category_name}")
    
    if not all_products:
        print("🔄 No se obtuvieron datos de ninguna categoría, usando datos de ejemplo...")
        return create_sample_data_all_categories()
    
    print(f"📊 Total de productos obtenidos: {len(all_products)}")
    return all_products


def create_sample_data_all_categories() -> List[Dict[str, Any]]:
    """
    Crea datos de ejemplo para todas las categorías cuando la API no está disponible.
    Incluye productos con diferentes niveles de descuento para probar la lógica.
    
    Returns:
        Lista de productos de ejemplo de todas las categorías
    """
    print("📝 Generando datos de ejemplo para todas las categorías...")
    return [
        # Smartphones
        {
            "id": "MLA123456789",
            "title": "Samsung Galaxy S23 Ultra 256GB Negro",
            "price": 799999,  # Precio con descuento
            "original_price": 999999,  # Precio original
            "currency_id": "ARS",
            "thumbnail": "https://http2.mlstatic.com/D_NQ_NP_123456-MLA123456789_012023-O.jpg",
            "permalink": "https://articulo.mercadolibre.com.ar/MLA-123456789-samsung-galaxy-s23-ultra-256gb-negro-_JM",
            "sold_quantity": 15,
            "category": "Smartphones"
        },
        {
            "id": "MLA987654321",
            "title": "iPhone 14 Pro Max 128GB Azul",
            "price": 1099999,  # Precio con descuento
            "original_price": 1299999,  # Precio original
            "currency_id": "ARS",
            "thumbnail": "https://http2.mlstatic.com/D_NQ_NP_987654-MLA987654321_012023-O.jpg",
            "permalink": "https://articulo.mercadolibre.com.ar/MLA-987654321-iphone-14-pro-max-128gb-azul-_JM",
            "sold_quantity": 8,
            "category": "Smartphones"
        },
        # Tablets
        {
            "id": "MLA111222333",
            "title": "iPad Air 5 64GB WiFi Gris Espacial",
            "price": 599999,  # Precio con descuento
            "original_price": 799999,  # Precio original
            "currency_id": "ARS",
            "thumbnail": "https://http2.mlstatic.com/D_NQ_NP_111222-MLA111222333_012023-O.jpg",
            "permalink": "https://articulo.mercadolibre.com.ar/MLA-111222333-ipad-air-5-64gb-wifi-gris-espacial-_JM",
            "sold_quantity": 12,
            "category": "Tablets"
        },
        {
            "id": "MLA222333444",
            "title": "Samsung Galaxy Tab S8 128GB WiFi Negro",
            "price": 449999,  # Precio con descuento
            "original_price": 599999,  # Precio original
            "currency_id": "ARS",
            "thumbnail": "https://http2.mlstatic.com/D_NQ_NP_222333-MLA222333444_012023-O.jpg",
            "permalink": "https://articulo.mercadolibre.com.ar/MLA-222333444-samsung-galaxy-tab-s8-128gb-wifi-negro-_JM",
            "sold_quantity": 6,
            "category": "Tablets"
        },
        # Smartwatches
        {
            "id": "MLA333444555",
            "title": "Apple Watch Series 8 GPS 45mm Azul",
            "price": 299999,  # Precio con descuento
            "original_price": 399999,  # Precio original
            "currency_id": "ARS",
            "thumbnail": "https://http2.mlstatic.com/D_NQ_NP_333444-MLA333444555_012023-O.jpg",
            "permalink": "https://articulo.mercadolibre.com.ar/MLA-333444555-apple-watch-series-8-gps-45mm-azul-_JM",
            "sold_quantity": 9,
            "category": "Smartwatches"
        },
        {
            "id": "MLA444555666",
            "title": "Samsung Galaxy Watch 5 44mm Negro",
            "price": 199999,  # Precio con descuento
            "original_price": 299999,  # Precio original
            "currency_id": "ARS",
            "thumbnail": "https://http2.mlstatic.com/D_NQ_NP_444555-MLA444555666_012023-O.jpg",
            "permalink": "https://articulo.mercadolibre.com.ar/MLA-444555666-samsung-galaxy-watch-5-44mm-negro-_JM",
            "sold_quantity": 14,
            "category": "Smartwatches"
        },
        # Portátiles
        {
            "id": "MLA555666777",
            "title": "MacBook Air M2 13 pulgadas 256GB Gris Espacial",
            "price": 1299999,  # Precio con descuento
            "original_price": 1599999,  # Precio original
            "currency_id": "ARS",
            "thumbnail": "https://http2.mlstatic.com/D_NQ_NP_555666-MLA555666777_012023-O.jpg",
            "permalink": "https://articulo.mercadolibre.com.ar/MLA-555666777-macbook-air-m2-13-pulgadas-256gb-gris-espacial-_JM",
            "sold_quantity": 3,
            "category": "Portátiles"
        },
        {
            "id": "MLA666777888",
            "title": "Dell XPS 13 512GB SSD 16GB RAM Negro",
            "price": 899999,  # Precio con descuento
            "original_price": 1199999,  # Precio original
            "currency_id": "ARS",
            "thumbnail": "https://http2.mlstatic.com/D_NQ_NP_666777-MLA666777888_012023-O.jpg",
            "permalink": "https://articulo.mercadolibre.com.ar/MLA-666777888-dell-xps-13-512gb-ssd-16gb-ram-negro-_JM",
            "sold_quantity": 7,
            "category": "Portátiles"
        },
        # Productos sin descuento (para probar filtrado)
        {
            "id": "MLA777888999",
            "title": "Xiaomi Redmi Note 12 Pro 128GB Blanco",
            "price": 249999,  # Sin descuento real
            "original_price": 249999,  # Sin descuento real
            "currency_id": "ARS",
            "thumbnail": "https://http2.mlstatic.com/D_NQ_NP_777888-MLA777888999_012023-O.jpg",
            "permalink": "https://articulo.mercadolibre.com.ar/MLA-777888999-xiaomi-redmi-note-12-pro-128gb-blanco-_JM",
            "sold_quantity": 25,
            "category": "Smartphones"
        }
    ]


def calculate_discount(original_price: float, current_price: float) -> float:
    """
    Calcula el porcentaje de descuento entre precio original y precio actual.
    
    Args:
        original_price: Precio original del producto
        current_price: Precio actual del producto
        
    Returns:
        Porcentaje de descuento redondeado a 2 decimales
    """
    if original_price <= 0 or current_price <= 0:
        return 0.0
    
    if current_price >= original_price:
        return 0.0
    
    discount = round((1 - (current_price / original_price)) * 100, 2)
    return discount


def transform_product_data(product: Dict[str, Any]) -> Dict[str, Any]:
    """
    Transforma los datos de un producto de MercadoLibre al formato requerido.
    Calcula descuentos y maneja precios originales vs actuales.
    
    Args:
        product: Diccionario con datos del producto de MercadoLibre
        
    Returns:
        Diccionario con datos transformados
    """
    # Obtener precios
    current_price = product.get("price", 0)
    original_price = product.get("original_price", current_price)  # Si no hay precio original, usar el actual
    
    # Calcular descuento
    discount_percentage = calculate_discount(original_price, current_price)
    
    return {
        "ProductId": product.get("id", ""),
        "Image Url": product.get("thumbnail", ""),
        "Video Url": "",  # dejar vacío si no hay
        "Product Desc": product.get("title", ""),
        "Origin Price": original_price,  # precio original si existe, si no usar price
        "Discount Price": current_price,  # precio actual
        "Discount": f"{discount_percentage}%" if discount_percentage > 0 else "",  # descuento calculado
        "Currency": product.get("currency_id", ""),
        "Commission Rate": "",
        "Commission": "",
        "Sales180Day": product.get("sold_quantity", 0),
        "Positive Feedback": "",
        "Promotion Url": product.get("permalink", ""),
        "Code Name": "",
        "Code Start Time": "",
        "Code End Time": "",
        "Code Value": "",
        "Code Quantity": "",
        "Code Minimum Spend": ""
    }


def filter_products_by_discount(products: List[Dict[str, Any]], min_discount: float = 10.0) -> List[Dict[str, Any]]:
    """
    Filtra productos que tengan un descuento mayor o igual al mínimo especificado.
    
    Args:
        products: Lista de productos transformados
        min_discount: Descuento mínimo requerido (porcentaje)
        
    Returns:
        Lista de productos filtrados
    """
    filtered_products = []
    
    for product in products:
        discount_str = product.get("Discount", "")
        if discount_str and discount_str.endswith("%"):
            try:
                discount_value = float(discount_str.replace("%", ""))
                if discount_value >= min_discount:
                    filtered_products.append(product)
            except ValueError:
                continue
    
    return filtered_products


def sort_products_by_discount(products: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Ordena productos por mayor descuento (descendente).
    
    Args:
        products: Lista de productos a ordenar
        
    Returns:
        Lista de productos ordenada por descuento
    """
    def get_discount_value(product):
        discount_str = product.get("Discount", "")
        if discount_str and discount_str.endswith("%"):
            try:
                return float(discount_str.replace("%", ""))
            except ValueError:
                return 0.0
        return 0.0
    
    return sorted(products, key=get_discount_value, reverse=True)


def process_mercadolibre_data(products: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Procesa los datos de todas las categorías, filtra por descuento y ordena por mayor descuento.
    
    Args:
        products: Lista de productos de todas las categorías
        
    Returns:
        Lista de productos transformados, filtrados y ordenados
    """
    transformed_products = []
    
    print(f"Procesando {len(products)} productos de todas las categorías...")
    
    for product in products:
        try:
            transformed_product = transform_product_data(product)
            transformed_products.append(transformed_product)
        except Exception as e:
            print(f"⚠️  Error procesando producto {product.get('id', 'unknown')}: {e}")
            continue
    
    print(f"✅ {len(transformed_products)} productos procesados exitosamente")
    
    # Filtrar productos con descuento >= 10%
    filtered_products = filter_products_by_discount(transformed_products, 10.0)
    print(f"🔍 {len(filtered_products)} productos con descuento >= 10%")
    
    # Ordenar por mayor descuento
    sorted_products = sort_products_by_discount(filtered_products)
    print(f"📊 Productos ordenados por mayor descuento")
    
    return sorted_products


def save_json_file(products: List[Dict[str, Any]], filename: str = "smarphone500json.json") -> None:
    """
    Guarda los productos en un archivo JSON.
    
    Args:
        products: Lista de productos transformados
        filename: Nombre del archivo JSON
    """
    try:
        # Guardar directamente como array de productos (formato original)
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(products, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Archivo {filename} guardado exitosamente con {len(products)} productos")
        
    except Exception as e:
        print(f"❌ Error al guardar archivo JSON: {e}")
        sys.exit(1)


def main():
    """
    Función principal que ejecuta todo el proceso de actualización.
    """
    print("🚀 Iniciando actualización del archivo JSON...")
    print(f"📅 Fecha y hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Obtener datos de todas las categorías
    all_products = fetch_all_categories()
    
    # Procesar y transformar datos
    processed_products = process_mercadolibre_data(all_products)
    
    # Guardar en archivo JSON
    save_json_file(processed_products)
    
    print("🎉 Actualización completada exitosamente!")


if __name__ == "__main__":
    main()
