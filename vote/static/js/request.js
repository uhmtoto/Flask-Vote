$(document).ready(function () {
    $('.vote').click(function () {
        c_name = $(this).attr('data-name')
        swal.mixin({
            input: 'text',
            inputAttributes: {
                autocapitalize: 'off'
            },
            showLoaderOnConfirm: true,
            confirmButtonText: '다음 &rarr;',
            showCancelButton: true,
            progressSteps: ['1', '2'],
            preConfirm: (login) => {
                return fetch('/vote')
                    .then(response => {
                        if (!response.ok) {
                            throw new Error(response.statusText)
                        }
                        if (response.text != 'ok') {
                            throw new Error(response.text)
                        }
                    })
                    .catch(error => {
                        swal.showValidationMessage(
                            '투표 과정에서 오류가 발생했습니다. 다시 한 번 시도해주세요.'
                        )
                    })
            },
            allowOutsideClick: () => !swal.isLoading()
        }).queue([
            '본인 확인 코드를 입력해주세요.',
            {
                title: '정말로 ' + c_name + ' 후보를 선택하시겠습니까?',
                text: '투표 후 결정을 바꿀 수 없습니다.'
            }
        ]).then((result) => {
            if (result.value) {
                swal({
                    title: '투표가 정상적으로 처리되었습니다!',
                    confirmButtonText: '창닫기'
                })
            }
        })
    });
});