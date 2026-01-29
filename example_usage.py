"""
Contoh penggunaan BPS Data Checker
"""

from bps_data_checker import BPSDataChecker
import json

def main():
    # Ganti dengan API key Anda
    API_KEY = 'f40723032cd619efc97acbc6a9a66272'

    # Inisialisasi checker untuk domain Gorontalo
    checker = BPSDataChecker(api_key=API_KEY, domain='7500')

    print("=== CONTOH PENGGUNAAN BPS DATA CHECKER ===\n")

    # 1. Mengecek satu jenis data tertentu
    print("1. Mengecek Static Tables saja:")
    static_result = checker.check_static_tables(limit=3)
    print(f"   Status: {static_result['status']}")
    print(f"   Total: {static_result['total_tables']} tables")
    print(f"   Sample titles: {[table['title'][:50] + '...' for table in static_result['sample_tables']]}")
    print()

    # 2. Mengecek Publications
    print("2. Mengecek Publications:")
    pub_result = checker.check_publications(limit=2)
    print(f"   Status: {pub_result['status']}")
    print(f"   Total: {pub_result['total_publications']} publications")
    if pub_result['sample_publications']:
        print(f"   Sample: {pub_result['sample_publications'][0].get('title', 'N/A')}")
    print()

    # 3. Mengecek untuk domain berbeda (contoh: Sumatera Utara)
    print("3. Mengecek data untuk domain Gorontalo (7500):")
    checker_sumatra = BPSDataChecker(api_key=API_KEY, domain='7500')
    sumatra_static = checker_sumatra.check_static_tables(limit=1)
    print(f"   Static Tables di Gorontalo: {sumatra_static['total_tables']} tables")
    print()

    # 4. Pengecekan lengkap untuk Gorontalo
    print("4. Pengecekan lengkap untuk Gorontalo:")
    full_results = checker.check_all_data_availability(limit_per_category=2)

    print("   Ringkasan ketersediaan data:")
    for category, data in full_results['data_availability'].items():
        if data['status'] == 'success':
            # Cari field jumlah total berdasarkan kategori yang tepat
            count = 0
            if category == 'static_tables' and 'total_tables' in data:
                count = data['total_tables']
            elif category == 'dynamic_tables' and 'total_tables' in data:
                count = data['total_tables']
            elif category == 'subjects' and 'total_subjects' in data:
                count = data['total_subjects']
            elif category == 'publications' and 'total_publications' in data:
                count = data['total_publications']
            elif category == 'press_releases' and 'total_press_releases' in data:
                count = data['total_press_releases']
            elif category == 'strategic_indicators' and 'total_indicators' in data:
                count = data['total_indicators']
            elif category == 'news' and 'total_news' in data:
                count = data['total_news']
            elif category == 'infographics' and 'total_infographics' in data:
                count = data['total_infographics']
            print(f"   - {category.replace('_', ' ').title()}: {count} items")
        else:
            print(f"   - {category.replace('_', ' ').title()}: Error")

    # 5. Simpan hasil ke file
    filename = checker.save_results_to_json(full_results, 'contoh_hasil_cek_gorontalo.json')
    print(f"\n   Hasil lengkap disimpan ke: {filename}")

    print("\n=== SELESAI ===")

if __name__ == "__main__":
    main()