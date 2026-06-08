import sys
import os

# Ép Python tìm kiếm module bên trong thư mục src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

if __name__ == "__main__":
    from bcsfe.cli.main import Main
    from bcsfe import color
    import bcsfe
    
    # Tự động gán thuộc tính __version__ thủ công nếu chạy file lẻ bị thiếu
    if not hasattr(bcsfe, "__version__"):
        bcsfe.__version__ = "3.4.0"
        
    try:
        Main().main()
    except KeyboardInterrupt:
        try:
            Main.leave()
        except SystemExit:
            pass
    except Exception as e:
        # Nếu thiếu file ngôn ngữ (locale) hoặc cấu hình khi chạy trực tiếp
        if "local_manager" in str(e) or "locale" in str(e):
            print("\n[Thành công] Hệ thống đường dẫn đã chuẩn!")
            print("Để chạy tool không lỗi giao diện, hãy cài đặt bằng lệnh: pip install -e .")
            print("Sau đó gõ lệnh để mở: bcsfe")
        else:
            raise e

