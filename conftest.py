import os
import pytest
from datetime import datetime
from playwright.sync_api import sync_playwright


@pytest.fixture
def page(request):
    with sync_playwright() as playwright:
        video_dir = f"videos"
        recording_data = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(record_video_dir=video_dir,
                                      record_video_size={"width": 1280, "height": 720}
                                      )
        config_page = context.new_page()

        # Зададим более информативный вариант имени записываемого видео
        video_path = config_page.video.path()
        new_video_path = os.path.join(video_dir, f"{request.node.name}_{recording_data}.webm")
        yield config_page
        context.close()

        # Переименуем файл с записанным видео
        os.rename(video_path, new_video_path)
        browser.close()
