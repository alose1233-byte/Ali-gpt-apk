name: Build APK
on: [push, pull_request, workflow_dispatch]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Get Date
        id: get-date
        run: |
          echo "date=$(date +'%Y-%m-%d')" >> $GITHUB_OUTPUT
      - name: Cache Buildozer
        uses: actions/cache@v4
        with:
          path: .buildozer
          key: ${{ runner.os }}-buildozer-${{ hashFiles('buildozer.spec') }}-${{ steps.get-date.outputs.date }}
      - name: Build with Buildozer
        uses: herreraj/buildozer-action@master
        with:
          command: buildozer android debug
          buildozer_version: master
      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: package
          path: bin/*.apk
