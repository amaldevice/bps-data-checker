"""
BPS Data Availability Checker untuk Domain Gorontalo (7500)
Fungsi sederhana untuk mengecek ketersediaan berbagai jenis data BPS
"""

import stadata
import requests
import json
import pandas as pd
from datetime import datetime
import sys
import os

# Add stadata folder to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'stadata'))

class BPSDataChecker:
    """
    Kelas untuk mengecek ketersediaan data BPS di berbagai kategori
    """

    def __init__(self, api_key, domain="7500"):
        """
        Inisialisasi dengan API key dan domain BPS

        Args:
            api_key (str): API key dari WebAPI BPS
            domain (str): Domain ID BPS (default: "7500" untuk Gorontalo)
        """
        self.api_key = api_key
        self.domain = domain
        self.base_url = "https://webapi.bps.go.id/v1/api"
        self.client = stadata.Client(api_key)

    def check_static_tables(self, limit=10):
        """
        Mengecek ketersediaan Static Tables

        Args:
            limit (int): Jumlah maksimal data yang ditampilkan

        Returns:
            dict: Informasi ketersediaan static tables
        """
        try:
            print(f"[CHECKING] Mengecek Static Tables untuk domain {self.domain}...")

            # Menggunakan stadata library
            data = self.client.list_statictable(all=False, domain=[self.domain])

            # Perbaiki pengecekan DataFrame
            total_count = 0
            sample_data = []
            if data is not None and not data.empty:
                total_count = len(data)
                sample_data = data.head(limit).to_dict('records')

            result = {
                'status': 'success',
                'total_tables': total_count,
                'sample_tables': sample_data,
                'last_checked': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

            print(f"[SUCCESS] Ditemukan {total_count} Static Tables")
            return result

        except Exception as e:
            print(f"[ERROR] Error checking static tables: {str(e)}")
            return {
                'status': 'error',
                'error': str(e),
                'last_checked': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

    def check_dynamic_tables(self, limit=10):
        """
        Mengecek ketersediaan Dynamic Tables (Data)

        Args:
            limit (int): Jumlah maksimal data yang ditampilkan

        Returns:
            dict: Informasi ketersediaan dynamic tables
        """
        try:
            print(f"[CHECKING] Mengecek Dynamic Tables untuk domain {self.domain}...")

            # Menggunakan stadata library
            data = self.client.list_dynamictable(all=False, domain=[self.domain])

            # Perbaiki pengecekan DataFrame
            total_count = 0
            sample_data = []
            if data is not None and not data.empty:
                total_count = len(data)
                sample_data = data.head(limit).to_dict('records')

            result = {
                'status': 'success',
                'total_tables': total_count,
                'sample_tables': sample_data,
                'last_checked': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

            print(f"[SUCCESS] Ditemukan {total_count} Dynamic Tables")
            return result

        except Exception as e:
            print(f"[ERROR] Error checking dynamic tables: {str(e)}")
            return {
                'status': 'error',
                'error': str(e),
                'last_checked': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

    def check_publications(self, limit=10):
        """
        Mengecek ketersediaan Publications

        Args:
            limit (int): Jumlah maksimal data yang ditampilkan

        Returns:
            dict: Informasi ketersediaan publications
        """
        try:
            print(f"[CHECKING] Mengecek Publications untuk domain {self.domain}...")

            # Menggunakan requests langsung karena stadata mungkin belum support
            url = f"{self.base_url}/list/model/publication/domain/{self.domain}/key/{self.api_key}"
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()

            total_count = 0
            if 'data' in data and len(data['data']) > 1:
                # Data biasanya ada di index 1 dari array data
                publications = data['data'][1] if len(data['data']) > 1 else []
                total_count = len(publications)

            result = {
                'status': 'success',
                'total_publications': total_count,
                'sample_publications': publications[:limit] if publications else [],
                'api_response': data,
                'last_checked': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

            print(f"[SUCCESS] Ditemukan {total_count} Publications")
            return result

        except Exception as e:
            print(f"[ERROR] Error checking publications: {str(e)}")
            return {
                'status': 'error',
                'error': str(e),
                'last_checked': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

    def check_press_releases(self, limit=10):
        """
        Mengecek ketersediaan Press Releases

        Args:
            limit (int): Jumlah maksimal data yang ditampilkan

        Returns:
            dict: Informasi ketersediaan press releases
        """
        try:
            print(f"[CHECKING] Mengecek Press Releases untuk domain {self.domain}...")

            # Menggunakan requests langsung
            url = f"{self.base_url}/list/model/pressrelease/domain/{self.domain}/key/{self.api_key}"
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()

            total_count = 0
            if 'data' in data and len(data['data']) > 1:
                press_releases = data['data'][1] if len(data['data']) > 1 else []
                total_count = len(press_releases)

            result = {
                'status': 'success',
                'total_press_releases': total_count,
                'sample_press_releases': press_releases[:limit] if press_releases else [],
                'api_response': data,
                'last_checked': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

            print(f"[SUCCESS] Ditemukan {total_count} Press Releases")
            return result

        except Exception as e:
            print(f"[ERROR] Error checking press releases: {str(e)}")
            return {
                'status': 'error',
                'error': str(e),
                'last_checked': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

    def check_strategic_indicators(self, limit=10):
        """
        Mengecek ketersediaan Strategic Indicators

        Args:
            limit (int): Jumlah maksimal data yang ditampilkan

        Returns:
            dict: Informasi ketersediaan strategic indicators
        """
        try:
            print(f"[CHECKING] Mengecek Strategic Indicators untuk domain {self.domain}...")

            # Menggunakan requests langsung
            url = f"{self.base_url}/list/model/strategicindicator/domain/{self.domain}/key/{self.api_key}"
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()

            total_count = 0
            indicators_data = []
            if 'data' in data and len(data['data']) > 1:
                indicators_data = data['data'][1] if len(data['data']) > 1 else []
                total_count = len(indicators_data)

            result = {
                'status': 'success',
                'total_indicators': total_count,
                'sample_indicators': indicators_data[:limit] if indicators_data else [],
                'api_response': data,
                'last_checked': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

            print(f"[SUCCESS] Ditemukan {total_count} Strategic Indicators")
            return result

        except Exception as e:
            print(f"[ERROR] Error checking strategic indicators: {str(e)}")
            return {
                'status': 'error',
                'error': str(e),
                'last_checked': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

    def check_news(self, limit=10):
        """
        Mengecek ketersediaan News/Berita BPS

        Args:
            limit (int): Jumlah maksimal data yang ditampilkan

        Returns:
            dict: Informasi ketersediaan news
        """
        try:
            print(f"[CHECKING] Mengecek News untuk domain {self.domain}...")

            # Menggunakan requests langsung
            url = f"{self.base_url}/list/model/news/domain/{self.domain}/key/{self.api_key}"
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()

            total_count = 0
            news_data = []
            if 'data' in data and len(data['data']) > 1:
                news_data = data['data'][1] if len(data['data']) > 1 else []
                total_count = len(news_data)

            result = {
                'status': 'success',
                'total_news': total_count,
                'sample_news': news_data[:limit] if news_data else [],
                'api_response': data,
                'last_checked': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

            print(f"[SUCCESS] Ditemukan {total_count} News")
            return result

        except Exception as e:
            print(f"[ERROR] Error checking news: {str(e)}")
            return {
                'status': 'error',
                'error': str(e),
                'last_checked': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

    def check_infographics(self, limit=10):
        """
        Mengecek ketersediaan Infographics

        Args:
            limit (int): Jumlah maksimal data yang ditampilkan

        Returns:
            dict: Informasi ketersediaan infographics
        """
        try:
            print(f"[CHECKING] Mengecek Infographics untuk domain {self.domain}...")

            # Menggunakan requests langsung
            url = f"{self.base_url}/list/model/infographic/domain/{self.domain}/key/{self.api_key}"
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()

            total_count = 0
            if 'data' in data and len(data['data']) > 1:
                infographics = data['data'][1] if len(data['data']) > 1 else []
                total_count = len(infographics)

            result = {
                'status': 'success',
                'total_infographics': total_count,
                'sample_infographics': infographics[:limit] if infographics else [],
                'api_response': data,
                'last_checked': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

            print(f"[SUCCESS] Ditemukan {total_count} Infographics")
            return result

        except Exception as e:
            print(f"[ERROR] Error checking infographics: {str(e)}")
            return {
                'status': 'error',
                'error': str(e),
                'last_checked': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

    def check_subjects(self, limit=10):
        """
        Mengecek ketersediaan Subjects

        Args:
            limit (int): Jumlah maksimal data yang ditampilkan

        Returns:
            dict: Informasi ketersediaan subjects
        """
        try:
            print(f"[CHECKING] Mengecek Subjects untuk domain {self.domain}...")

            # Menggunakan requests langsung karena stadata tidak punya list_subject
            url = f"{self.base_url}/list/model/subject/domain/{self.domain}/key/{self.api_key}"
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()

            total_count = 0
            subjects = []
            if 'data' in data and len(data['data']) > 1:
                subjects = data['data'][1] if len(data['data']) > 1 else []
                total_count = len(subjects)

            result = {
                'status': 'success',
                'total_subjects': total_count,
                'sample_subjects': subjects[:limit] if subjects else [],
                'api_response': data,
                'last_checked': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

            print(f"[SUCCESS] Ditemukan {total_count} Subjects")
            return result

        except Exception as e:
            print(f"[ERROR] Error checking subjects: {str(e)}")
            return {
                'status': 'error',
                'error': str(e),
                'last_checked': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

    def check_all_data_availability(self, limit_per_category=5):
        """
        Mengecek ketersediaan semua jenis data BPS secara menyeluruh

        Args:
            limit_per_category (int): Jumlah maksimal sample per kategori

        Returns:
            dict: Ringkasan ketersediaan semua data BPS
        """
        print("[START] Memulai pengecekan ketersediaan data BPS untuk Domain Gorontalo (7500)")
        print("=" * 70)

        results = {
            'domain': self.domain,
            'domain_name': 'Gorontalo',
            'check_timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'data_availability': {}
        }

        # Daftar fungsi checking yang akan dijalankan
        check_functions = [
            ('static_tables', self.check_static_tables),
            ('dynamic_tables', self.check_dynamic_tables),
            ('subjects', self.check_subjects),
            ('publications', self.check_publications),
            ('press_releases', self.check_press_releases),
            ('strategic_indicators', self.check_strategic_indicators),
            ('news', self.check_news),
            ('infographics', self.check_infographics)
        ]

        # Jalankan semua pengecekan
        for category_name, check_function in check_functions:
            try:
                result = check_function(limit=limit_per_category)
                results['data_availability'][category_name] = result
                print(f"[DATA] {category_name.replace('_', ' ').title()}: {'[SUCCESS] Available' if result['status'] == 'success' else '[ERROR] Error'}")
            except Exception as e:
                results['data_availability'][category_name] = {
                    'status': 'error',
                    'error': str(e),
                    'last_checked': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                print(f"[DATA] {category_name.replace('_', ' ').title()}: [ERROR] Error - {str(e)}")

        print("
" + "=" * 70)
        print("[SUCCESS] Pengecekan selesai!")
        return results

    def save_results_to_json(self, results, filename=None):
        """
        Menyimpan hasil pengecekan ke file JSON

        Args:
            results (dict): Hasil dari check_all_data_availability
            filename (str): Nama file (optional, default akan menggunakan timestamp)
        """
        if filename is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"bps_data_availability_{self.domain}_{timestamp}.json"

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)

        print(f"[SAVE] Hasil disimpan ke: {filename}")
        return filename


def main():
    """
    Fungsi utama untuk testing
    """
    # Ganti dengan API key Anda
    API_KEY = 'f40723032cd619efc97acbc6a9a66272'  # API key dari project existing

    # Inisialisasi checker
    checker = BPSDataChecker(api_key=API_KEY, domain='7500')

    # Jalankan pengecekan menyeluruh
    results = checker.check_all_data_availability()

    # Simpan hasil ke file
    checker.save_results_to_json(results)

    # Tampilkan ringkasan
    print("
[SUMMARY] RINGKASAN KETERSEDIAAN DATA BPS GORONTALO")
    print("=" * 50)

    for category, data in results['data_availability'].items():
        if data['status'] == 'success':
            # Cari field yang menunjukkan jumlah total
            total_field = None
            if 'total_tables' in data:
                total_field = 'total_tables'
            elif 'total_publications' in data:
                total_field = 'total_publications'
            elif 'total_press_releases' in data:
                total_field = 'total_press_releases'
            elif 'total_indicators' in data:
                total_field = 'total_indicators'
            elif 'total_news' in data:
                total_field = 'total_news'
            elif 'total_infographics' in data:
                total_field = 'total_infographics'
            elif 'total_subjects' in data:
                total_field = 'total_subjects'

            if total_field:
                print(f"[DATA] {category.replace('_', ' ').title()}: {data[total_field]} items")
            else:
                print(f"[DATA] {category.replace('_', ' ').title()}: Available")
        else:
            print(f"[DATA] {category.replace('_', ' ').title()}: Error - {data.get('error', 'Unknown error')}")


if __name__ == "__main__":
    main()